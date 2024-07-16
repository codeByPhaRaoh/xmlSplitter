
# split_xml.py

## Overview

`split_xml.py` is a Python script designed to split a large XML file into smaller XML files based on a specified maximum size in megabytes (MB). The script ensures that the resulting XML files are well-formed by wrapping the split elements in a root element.

## Features

- Splits large XML files into smaller, manageable files.
- Allows specifying the maximum size of each split file in MB.
- Ensures the split files are well-formed XML documents.
- Automatically creates the output directory if it does not exist.

## Requirements

- Python 3.x
- `xml.etree.ElementTree` module (comes with the standard library)

## Usage

1. **Set up the script:**
   - Ensure you have Python 3.x installed on your system.
   - Save the `split_xml.py` script to your working directory.

2. **Prepare your XML file:**
   - Place the XML file you want to split in the same directory as the script or provide the full path to the file.

3. **Run the script:**
   - Modify the `file_path`, `max_size_mb`, and `output_dir` variables in the script as needed.
   - Execute the script using Python.

### Example

```python
# Example usage
file_path = 'supp2024.xml'      # Path to the input XML file
max_size_mb = 10                # Maximum size of each split file in MB
output_dir = 'output_supp2024'  # Directory to save the split files

split_xml_file_by_size(file_path, max_size_mb, output_dir)
```

### Command Line

Alternatively, you can modify and run the script from the command line:

```sh
python split_xml.py
```

Ensure you have set the appropriate values for `file_path`, `max_size_mb`, and `output_dir` within the script before running it.

## Function Description

### `split_xml_file_by_size(file_path, max_size_mb, output_dir)`

- **Parameters:**
  - `file_path` (str): The path to the XML file to be split.
  - `max_size_mb` (int): The maximum size of each split file in megabytes.
  - `output_dir` (str): The directory where the split files will be saved.

- **Functionality:**
  - The function checks if the output directory exists; if not, it creates it.
  - It calculates the maximum size in bytes.
  - The XML file is parsed, and elements are added to new files until the size limit is reached.
  - The resulting files are saved in the specified output directory.

## License

This script is provided "as is" without any warranties. You are free to use and modify it as needed.

## Author

[Your Name]

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## Acknowledgments

This script utilizes the `xml.etree.ElementTree` module from the Python standard library.
