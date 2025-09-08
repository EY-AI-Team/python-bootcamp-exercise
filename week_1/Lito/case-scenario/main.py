import sys
import os

os.chdir(sys.path[0])

from file_reader import file_reader
from file_writer import file_writer

try:
    reader = file_reader()
    success = reader.read_file()
    
    if success:
        # get excel content
        content = reader.get_content()
        # execute json file writer
        writer = file_writer(content)
        dynamic_path: str = os.path.dirname(__file__)
        json_filepath: str = os.path.join(dynamic_path, 'output.json')
        write_success = writer.write_to_file(json_filepath)
        
        if write_success:
            print("File written successfully.")
        else:
            print("Failed to write the file.")
    else:
        print("Failed to read the file.")


except Exception as e:
    print(f"An error occurred: {e}")