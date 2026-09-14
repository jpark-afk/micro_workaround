@echo off
setlocal

REM Patches a raw customer DDS XML with the parts a fresh export is missing
REM (schema location, qos_profile domain_participant_qos, and the
REM application/node/deployment overlay), all from built-in templates.
REM Usage:
REM   patch_missing_part_hkmc.bat [source_xml] [output_xml] [autosar_participant] [schema_location]

set "SOURCE_XML=%~1"
set "OUTPUT_XML=%~2"
set "AUTOSAR_PARTICIPANT=%~3"
set "SCHEMA_LOCATION=%~4"

if "%SOURCE_XML%"=="" set "SOURCE_XML=%~dp0..\..\slcorp04\CODA Master Interface_PDIO_FL_v5.5.xml"
if "%OUTPUT_XML%"=="" set "OUTPUT_XML=%~dp0..\..\slcorp04\test_system.xml"
if "%AUTOSAR_PARTICIPANT%"=="" set "AUTOSAR_PARTICIPANT=PDIO_FL::Domain_6"

if not exist "%SOURCE_XML%" (
    echo ERROR: source XML not found: "%SOURCE_XML%"
    exit /b 1
)

set "OUTPUT_ARG="
if not "%OUTPUT_XML%"=="" set "OUTPUT_ARG=--output "%OUTPUT_XML%""
set "SCHEMA_ARG="
if not "%SCHEMA_LOCATION%"=="" set "SCHEMA_ARG=--schema-location "%SCHEMA_LOCATION%""

python "%~dp0patch_missing_part_hkmc.py" --source "%SOURCE_XML%" --autosar-participant "%AUTOSAR_PARTICIPANT%" %OUTPUT_ARG% %SCHEMA_ARG%

if errorlevel 1 (
    echo ERROR: missing-part patch failed.
    exit /b 1
)

endlocal
exit /b 0
