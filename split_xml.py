import xml.etree.ElementTree as ET
import os

def split_xml_file_by_size(file_path, max_size_mb, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    max_size_bytes = max_size_mb * 1024 * 1024
    file_index = 0
    current_size = 0
    root_element = None
    current_file = None
    
    def start_new_file():
        nonlocal file_index, current_size, root_element, current_file
        if current_file:
            current_file.write(ET.tostring(root_element, encoding='unicode'))
            current_file.close()
        
        file_index += 1
        current_size = 0
        root_element = ET.Element('root')
        current_file = open(os.path.join(output_dir, f'split_file_{file_index}.xml'), 'w', encoding='utf-8')
        current_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')

    tree = ET.parse(file_path)
    root = tree.getroot()
    
    start_new_file()
    
    for element in root:
        element_size = len(ET.tostring(element, encoding='unicode'))
        if current_size + element_size > max_size_bytes:
            start_new_file()
        
        root_element.append(element)
        current_size += element_size
    
    if current_file:
        current_file.write(ET.tostring(root_element, encoding='unicode'))
        current_file.close()

# Example usage
file_path = ''
max_size_mb = 500
output_dir = ''

split_xml_file_by_size(file_path, max_size_mb, output_dir)
