# arxml-model-element-finder

A Python script that searches for elements in AUTOSAR Adaptive ARXML files by their SHORT-NAME and finds both definitions and references.

## Features

- Searches recursively through directories for ARXML files
- Finds exact matches of SHORT-NAME definitions
- Identifies references to the SHORT-NAME in other files
- Reports the full reference paths and element types
- Handles XML parsing errors gracefully

## Requirements

- Python 3.6 or higher
- Supported AUTOSAR Adaptive release: R20-11
- Supported AUTOSAR Schema: 00049
- No additional dependencies required (uses standard library only)

## Usage

1. Run the script:
```bash
python find_arxml_element.py
```

2. When prompted:
   - Enter the directory path containing ARXML files
   - Enter the SHORT-NAME you want to search for

## Example Output

```
Enter the directory path containing ARXML files: /workspaces/work
Enter the SHORT-NAME to search for: SifMyService

The short-name 'SifMyService' is defined in:
  /workspaces/work/ap-sif/model/SifMyService.arxml

References where 'SifMyService' is used:

In file: /workspaces/work/ap-sif/ServiceInterfaceDeployment_SipSidMyService.arxml
  Element: SERVICE-INTERFACE-REF
  Path: /AP/DataDictionary/ServiceInterfaces/SifMyService

In file: /workspaces/work/ap-exe-app1/model/ApplicationManifest_App1.arxml
  Element: PROVIDED-INTERFACE-TREF
  Path: /AP/DataDictionary/ServiceInterfaces/SifMyService

In file: /workspaces/work/ap-exe-app2/model/ApplicationManifest_App2.arxml
  Element: REQUIRED-INTERFACE-TREF
  Path: /AP/DataDictionary/ServiceInterfaces/SifMyService
```

## Error Handling

The script will:
- Skip files that cannot be parsed
- Display error messages for problematic files
- Continue processing remaining files even if errors occur
- May or may not work with AUTOSAR Classic ARXML files
- Adaptations required for higher schema versions

## License

MIT License
