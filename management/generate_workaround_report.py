#!/usr/bin/env python3
"""Generate workaround report from workaround marker files under common folders.

The report scans for workaround tags in the form `workaround#CLASS` (case-insensitive),
extracts nearby context lines, and writes a Markdown report.
"""

from __future__ import annotations

import argparse
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Iterable

WORKAROUND_PATTERN = re.compile(r"workaround#(?:\s*([A-Za-z0-9_]+))?", re.IGNORECASE)
CONNEXT_MICRO_VERSION = "4.0.0_ER738"
DEFAULT_SOURCE_DIRS = ("templates", "fix_psl")
DEFAULT_OUTPUT = Path("workaround_report.md")

CATEGORY_DEFINITIONS = {
    "COMMON": "Mandatory patch.",
    "HAE": "For Autoever only; not a mandatory patch.",
    "VTT": "For virtual target (internal only); not a mandatory patch.",
}


class Occurrence:
    def __init__(
        self,
        file_path: Path,
        line_no: int,
        category: str,
        context_start: int,
        context_end: int,
        lines: list[str],
    ) -> None:
        self.file_path = file_path
        self.line_no = line_no
        self.category = category
        self.context_start = context_start
        self.context_end = context_end
        self.lines = lines


def read_text_with_fallback(path: Path) -> str:
    """Read text with a few common encodings used in mixed Windows projects."""
    for encoding in ("utf-8-sig", "utf-8", "cp949", "cp1252", "latin-1"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return path.read_text(encoding="utf-8", errors="replace")


def normalize_category(raw_category: str | None) -> str:
    if not raw_category:
        return "COMMON"
    category = raw_category.strip().upper()
    return category if category else "COMMON"


def display_path(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def find_xml_comment_end(lines: list[str], start_line: int) -> int:
    """Return the line number where an XML comment ends, or start_line if not a block."""
    line_text = lines[start_line - 1]
    if "<!--" not in line_text:
        return start_line
    if "-->" in line_text:
        return start_line

    for line_no in range(start_line + 1, len(lines) + 1):
        if "-->" in lines[line_no - 1]:
            return line_no

    return start_line


def collect_occurrences(source_dirs: Iterable[Path], context_lines: int, exclude_paths: Iterable[Path]) -> list[Occurrence]:
    occurrences: list[Occurrence] = []
    excluded = {path.resolve() for path in exclude_paths}
    seen_files: set[Path] = set()

    for source_dir in source_dirs:
        for source_file in sorted(source_dir.rglob("*"), key=lambda p: str(p).lower()):
            source_file = source_file.resolve()
            if not source_file.is_file() or source_file in excluded or source_file in seen_files:
                continue

            seen_files.add(source_file)
            content = read_text_with_fallback(source_file)
            lines = content.splitlines()

            for idx, line in enumerate(lines, start=1):
                if "workaround#" not in line.lower():
                    continue

                for match in WORKAROUND_PATTERN.finditer(line):
                    category = normalize_category(match.group(1))
                    start = max(1, idx - context_lines)
                    xml_comment_end = find_xml_comment_end(lines, idx)
                    end = min(len(lines), max(idx + context_lines, xml_comment_end + context_lines))
                    snippet = lines[start - 1 : end]
                    occurrences.append(
                        Occurrence(
                            file_path=source_file,
                            line_no=idx,
                            category=category,
                            context_start=start,
                            context_end=end,
                            lines=snippet,
                        )
                    )

    return occurrences


def build_category_summary(counts: Counter) -> str:
    if not counts:
        return "None"

    preferred_order = ["COMMON", "HAE", "VTT"]
    seen = set()
    parts: list[str] = []

    for category in preferred_order:
        if category in counts:
            parts.append(f"{category} ({counts[category]})")
            seen.add(category)

    for category in sorted(counts):
        if category not in seen:
            parts.append(f"{category} ({counts[category]})")

    return ", ".join(parts)


def build_report(
    source_label: str,
    occurrences: Iterable[Occurrence],
    workspace_root: Path,
    generated_at: datetime,
) -> str:
    items = list(occurrences)
    counts = Counter(item.category for item in items)

    lines: list[str] = []
    lines.append("# RTI workaround report")
    lines.append("")
    lines.append(f"## Generated date: {generated_at.strftime('%Y-%m-%d')}")
    lines.append("")
    lines.append(f"## Baseline Connext Micro version: {CONNEXT_MICRO_VERSION}")
    lines.append("")
    lines.append("**Workaround Report -- snippets with context and line numbers**")
    lines.append("")
    lines.append(f"- Scope: collected `workaround#` occurrences from all files under {source_label}.")
    lines.append(f"- Total items found: {len(items)}")
    lines.append(f"- Categories: {build_category_summary(counts)}")
    lines.append("")
    lines.append("Category definitions:")

    definition_order = ["COMMON", "HAE", "VTT"]
    for category in definition_order:
        definition = CATEGORY_DEFINITIONS[category]
        lines.append(f"- **{category}**: {definition}")

    unknown_categories = [category for category in sorted(counts) if category not in CATEGORY_DEFINITIONS]
    for category in unknown_categories:
        lines.append(f"- **{category}**: Unclassified category found in source comments.")

    lines.append("")
    lines.append("Below are code snippets (about +/-5 lines) around each `workaround#` occurrence. Items are grouped by category in this order: COMMON, HAE, VTT.")
    lines.append("")

    grouped: dict[str, list[Occurrence]] = {}
    for item in items:
        grouped.setdefault(item.category, []).append(item)

    ordered_categories: list[str] = ["COMMON", "HAE", "VTT"]
    ordered_categories.extend(category for category in sorted(grouped) if category not in {"COMMON", "HAE", "VTT"})

    section_index = 1
    for category in ordered_categories:
        category_items = grouped.get(category, [])
        lines.append(f"### {category} ({len(category_items)})")
        lines.append("")

        if not category_items:
            lines.append("- No items")
            lines.append("")
            continue

        for item in category_items:
            relative_path = display_path(item.file_path, workspace_root)
            lines.append(f"{section_index}) File: {relative_path} (L{item.line_no})")
            lines.append(item.lines[item.line_no - item.context_start].strip())
            lines.append("```text")

            current_line = item.context_start
            for text in item.lines:
                lines.append(f"L{current_line}: {text}")
                current_line += 1

            lines.append("```")
            lines.append("")
            section_index += 1

    return "\n".join(lines).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate workaround report from marked source files")
    parser.add_argument(
        "--source",
        action="append",
        help="Folder to scan recursively. Can be specified multiple times (default: common/templates and common/fix_psl)",
    )
    parser.add_argument(
        "--output",
        help="Output markdown file path (default: common/workaround_report.md)",
    )
    parser.add_argument(
        "--context",
        type=int,
        default=5,
        help="Number of context lines before/after each match (default: 5)",
    )
    return parser.parse_args()


def resolve_path(value: str, base_dir: Path) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path.resolve()
    return (base_dir / path).resolve()


def main() -> int:
    args = parse_args()

    if args.context < 0:
        raise ValueError("--context must be >= 0")

    script_dir = Path(__file__).resolve().parent
    common_dir = script_dir.parent
    workspace_root = common_dir.parent
    source_dirs = [resolve_path(source, script_dir) for source in args.source] if args.source else [common_dir / source for source in DEFAULT_SOURCE_DIRS]
    output_file = resolve_path(args.output, script_dir) if args.output else common_dir / DEFAULT_OUTPUT

    for source_dir in source_dirs:
        if not source_dir.exists() or not source_dir.is_dir():
            raise FileNotFoundError(f"Source folder not found: {source_dir}")

    occurrences = collect_occurrences(source_dirs=source_dirs, context_lines=args.context, exclude_paths=[output_file])
    source_label = ", ".join(f"`{display_path(source_dir, workspace_root)}`" for source_dir in source_dirs)
    report = build_report(
        source_label=source_label,
        occurrences=occurrences,
        workspace_root=workspace_root,
        generated_at=datetime.now(),
    )

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(report, encoding="utf-8")

    print(f"Generated: {output_file}")
    print(f"Matches: {len(occurrences)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
