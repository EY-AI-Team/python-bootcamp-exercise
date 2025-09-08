import sys
import os

os.chdir(sys.path[0])

from file_reader import file_reader
from file_writer import file_writer

try:

    reader = file_reader()
    success = reader.read_file()

    if success:
        content = reader.get_content()
        # Transform: first row is field names, next rows are values
        if content and len(content) > 1:
            fields = content[0]
            data = [dict(zip(fields, row)) for row in content[1:]]
        else:
            data = []

        writer = file_writer(data)
        write_success = writer.write_to_file("c:\\temp\\output.json")   
        if write_success:
            print("File written successfully.")
        else:
            print("Failed to write the file.")
    else:
        print("Failed to read the file.")


except Exception as e:
    print(f"An error occurred: {e}")    



