import sys
import os

current_dir = os.getcwd()

#print(f"Current working directory: {current_dir}")

file_path ="PythonTraining.xlsx"

from file_reader import file_reader
from file_writer import file_writer

try:

    reader = file_reader()
    success = reader.read_file(file_path)

    if success:
        content = reader.get_content()        
        writer = file_writer(content)
        write_success = writer.write_to_file("output.json")
        
        if write_success:
            print("File written successfully.")
        else:
            print("Failed to write the file.")
    else:
        print("Failed to read the file.")


except Exception as e:
    print(f"An error occurred: {e}")    



