import os
import xml.etree.ElementTree as ET
from pathlib import Path

def get_path_last_segment(path):
    """Extract the last segment of a path"""
    return path.strip('/').split('/')[-1]

def find_element_in_arxml(directory_path, search_element):
    """
    Search for a SHORT-NAME element and its references in ARXML files
    
    Args:
        directory_path (str): Path to directory containing ARXML files
        search_element (str): Element SHORT-NAME to search for
    """
    namespaces = {'ar': 'http://autosar.org/schema/r4.0'}
    definition_files = []  # Files where the SHORT-NAME is defined
    reference_files = []   # Files where the SHORT-NAME is referenced
    
    # Collect all ARXML files
    arxml_files = []
    for root_dir, _, files in os.walk(directory_path):
        for filename in files:
            if filename.lower().endswith('.arxml'):
                arxml_files.append(os.path.join(root_dir, filename))

    # First pass: Find where the SHORT-NAME is defined
    for file_path in arxml_files:
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            for elem in root.iter():
                if elem.tag.endswith('}SHORT-NAME'):
                    # Case sensitive exact match
                    if elem.text == search_element:
                        definition_files.append(file_path)
                        break
                        
        except ET.ParseError as e:
            print(f"Error parsing {file_path}: {e}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    # Second pass: Find references
    for file_path in arxml_files:
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            for elem in root.iter():
                if elem.text and file_path not in definition_files:
                    # Check if the last segment of the path exactly matches
                    ref_text = elem.text.strip()
                    last_segment = get_path_last_segment(ref_text)
                    if last_segment == search_element:
                        reference_files.append((file_path, elem.tag.split('}')[-1], ref_text))
                        
        except ET.ParseError as e:
            print(f"Error parsing {file_path}: {e}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    # Print results
    if definition_files:
        print(f"\nThe short-name '{search_element}' is defined in:")
        for file_path in definition_files:
            print(f"  {file_path}")
    else:
        print(f"\nNo definition found for short-name '{search_element}'")

    if reference_files:
        print(f"\nReferences where '{search_element}' is used:")
        for file_path, tag, ref_path in reference_files:
            print(f"\nIn file: {file_path}")
            print(f"  Element: {tag}")
            print(f"  Path: {ref_path}")
    else:
        print(f"\nNo references found for '{search_element}'")

def main():
    directory = input("Enter the directory path containing ARXML files: ")
    element = input("Enter the SHORT-NAME to search for: ")
    
    if not os.path.isdir(directory):
        print("Invalid directory path!")
        return
    
    find_element_in_arxml(directory, element)

if __name__ == "__main__":
    main()
