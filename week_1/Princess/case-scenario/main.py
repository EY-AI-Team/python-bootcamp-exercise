import sys
import os

os.chdir(sys.path[0])

from file_reader import file_reader
from file_writer import file_writer

try:

    reader = file_reader()
    success = reader.read_file()
     
     # Uncomment to debug content after reading
    if success:
        content = reader.get_content()
        print("Type of content:", type(content))  # Debug: Check type
        writer = file_writer(content)
        write_success = writer.write_to_file(r"C:\Users\GW433QS\OneDrive - EY\Attachments\Desktop\Phyton Training\Week1\case-scenario\output.json")
        
        if write_success:
            print("File written successfully.")
        else:
            print("Failed to write the file.")

except Exception as e:
    import traceback
    print(f"An error occurred while writing to the file: {e}")
    traceback.print_exc()
    success = False


