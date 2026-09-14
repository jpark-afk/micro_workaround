#!/usr/bin/env python3
"""workaround#HAE - mobilgene cannot interpret RECORD-VALUE-SPECIFICATION"""
"""Create typed port initialization constants in DdsCddType.arxml."""
import argparse
import os
import tempfile
import xml.etree.ElementTree as ET


AUTOSAR_NAMESPACE = "http://autosar.org/schema/r4.0"
XSI_NAMESPACE = "http://www.w3.org/2001/XMLSchema-instance"


def qualified(local_name):
    return "{%s}%s" % (AUTOSAR_NAMESPACE, local_name)


def child_text(element, local_name):
    child = element.find(qualified(local_name))
    return child.text.strip() if child is not None and child.text else None


def parse_xml(path):
    parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
    return ET.parse(path, parser=parser)


def implementation_types(root):
    result = {}
    for data_type in root.iter(qualified("IMPLEMENTATION-DATA-TYPE")):
        type_name = child_text(data_type, "SHORT-NAME")
        if not type_name:
            continue
        if type_name in result:
            raise ValueError("duplicate IMPLEMENTATION-DATA-TYPE: " + type_name)
        sub_elements = data_type.find(qualified("SUB-ELEMENTS"))
        if sub_elements is None:
            continue
        members = sub_elements.findall(qualified("IMPLEMENTATION-DATA-TYPE-ELEMENT"))
        if not members:
            raise ValueError("structured type has no members: " + type_name)
        result[type_name] = len(members)
    return result


def direct_package(root, package_name):
    packages = root.find(qualified("AR-PACKAGES"))
    if packages is None:
        raise ValueError("top-level AR-PACKAGES not found")
    for package in packages.findall(qualified("AR-PACKAGE")):
        if child_text(package, "SHORT-NAME") == package_name:
            return packages, package
    return packages, None


def constants_package(root):
    packages, package = direct_package(root, "Constants")
    if package is not None:
        elements = package.find(qualified("ELEMENTS"))
        if elements is None:
            elements = ET.SubElement(package, qualified("ELEMENTS"))
        return elements

    package = ET.Element(qualified("AR-PACKAGE"))
    ET.SubElement(package, qualified("SHORT-NAME")).text = "Constants"
    elements = ET.SubElement(package, qualified("ELEMENTS"))

    insert_at = len(packages)
    for index, candidate in enumerate(packages):
        if child_text(candidate, "SHORT-NAME") == "ComponentTypes":
            insert_at = index
            break
    packages.insert(insert_at, package)
    return elements


def upsert_constant(elements, type_name, member_count):
    constant_name = type_name + "_Init"
    matching = [
        constant
        for constant in elements.findall(qualified("CONSTANT-SPECIFICATION"))
        if child_text(constant, "SHORT-NAME") == constant_name
    ]
    if len(matching) > 1:
        raise ValueError("duplicate CONSTANT-SPECIFICATION: " + constant_name)

    if matching:
        constant = matching[0]
        for child in list(constant):
            constant.remove(child)
    else:
        constant = ET.SubElement(elements, qualified("CONSTANT-SPECIFICATION"))

    ET.SubElement(constant, qualified("SHORT-NAME")).text = constant_name
    value_spec = ET.SubElement(constant, qualified("VALUE-SPEC"))
    record = ET.SubElement(value_spec, qualified("RECORD-VALUE-SPECIFICATION"))
    fields = ET.SubElement(record, qualified("FIELDS"))
    for _ in range(member_count):
        numerical = ET.SubElement(fields, qualified("NUMERICAL-VALUE-SPECIFICATION"))
        ET.SubElement(numerical, qualified("VALUE")).text = "0"
    return constant_name


def port_specs(root):
    ports = root.find(".//" + qualified("COMPLEX-DEVICE-DRIVER-SW-COMPONENT-TYPE") + "/" + qualified("PORTS"))
    if ports is None:
        raise ValueError("CDD PORTS not found")
    result = []
    for port in ports:
        port_name = child_text(port, "SHORT-NAME")
        if not port_name:
            continue
        for spec_name in ("NONQUEUED-RECEIVER-COM-SPEC", "NONQUEUED-SENDER-COM-SPEC"):
            for spec in port.findall(".//" + qualified(spec_name)):
                result.append((port_name, spec))
    return result


def indent_subtree(element, level=0):
    child_indent = "\n" + "  " * (level + 1)
    closing_indent = "\n" + "  " * level
    if len(element):
        if not element.text or not element.text.strip():
            element.text = child_indent
        for child in element:
            indent_subtree(child, level + 1)
            if not child.tail or not child.tail.strip():
                child.tail = child_indent
        element[-1].tail = closing_indent


def patch_receiver_init_values(types_root, cdd_root):
    type_members = implementation_types(types_root)
    specs = port_specs(cdd_root)
    if not specs:
        raise ValueError("no nonqueued port COM-SPEC elements found")

    port_types = []
    for port_name, spec in specs:
        data_ref = child_text(spec, "DATA-ELEMENT-REF")
        if not data_ref:
            raise ValueError("DATA-ELEMENT-REF not found for port: " + port_name)
        type_name = data_ref.rsplit("/", 1)[-1]
        if type_name not in type_members:
            raise ValueError("structured implementation type not found: " + type_name)
        init_value = spec.find(qualified("INIT-VALUE"))
        if init_value is None:
            raise ValueError("INIT-VALUE not found for port: " + port_name)
        port_types.append((port_name, init_value, type_name))

    elements = constants_package(cdd_root)
    constant_names = {}
    for type_name in dict.fromkeys(item[2] for item in port_types):
        constant_names[type_name] = upsert_constant(elements, type_name, type_members[type_name])

    for _, init_value, type_name in port_types:
        for child in list(init_value):
            init_value.remove(child)
        reference = ET.SubElement(init_value, qualified("CONSTANT-REFERENCE"))
        constant_ref = ET.SubElement(
            reference,
            qualified("CONSTANT-REF"),
            {"DEST": "CONSTANT-SPECIFICATION"},
        )
        constant_ref.text = "/Constants/" + constant_names[type_name]

    _, package = direct_package(cdd_root, "Constants")
    indent_subtree(package)
    package.tail = "\n"
    return [(port_name, type_name, type_members[type_name]) for port_name, _, type_name in port_types]


def write_xml(tree, path):
    directory = os.path.dirname(os.path.abspath(path))
    file_descriptor, temporary_path = tempfile.mkstemp(prefix="DdsCddType_", suffix=".arxml", dir=directory)
    os.close(file_descriptor)
    try:
        tree.write(temporary_path, encoding="utf-8", xml_declaration=True)
        os.replace(temporary_path, path)
    finally:
        if os.path.exists(temporary_path):
            os.remove(temporary_path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--types-arxml", required=True)
    parser.add_argument("--cdd-arxml", required=True)
    args = parser.parse_args()

    try:
        types_tree = parse_xml(args.types_arxml)
        cdd_tree = parse_xml(args.cdd_arxml)
        patched_ports = patch_receiver_init_values(types_tree.getroot(), cdd_tree.getroot())
        ET.register_namespace("", AUTOSAR_NAMESPACE)
        ET.register_namespace("xsi", XSI_NAMESPACE)
        write_xml(cdd_tree, args.cdd_arxml)
    except (ET.ParseError, OSError, ValueError) as error:
        parser.error(str(error))

    for port_name, type_name, member_count in patched_ports:
        print("Port init constant: %s -> %s_Init (%d fields)" % (port_name, type_name, member_count))


if __name__ == "__main__":
    main()