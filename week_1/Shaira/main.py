import sys
import os

os.chdir(sys.path[0])

from file_reader import file_reader_class
from file_writer import file_writer_class

try:
    filePath = 'C:\\Users\\uf189za\\OneDrive - EY\\Desktop\\Phyton Bootcamp\\Week1_PythonBootcamp\\Week1_Python_Activity\\case-scenario\\Input\\PythonTraining 1.xlsx'
    sheetName = 'Employee'
    outputFile = 'C:\\Users\\uf189za\\OneDrive - EY\\Desktop\\Phyton Bootcamp\\Week1_PythonBootcamp\\Week1_Python_Activity\\case-scenario\\Output\\employees.json'

    reader = file_reader_class()
    success = reader.read_file(filePath, sheetName)
 
    if success:
        content = reader.get_content()
        print(content)
        
        writer = file_writer_class(content)
        write_success = writer.write_to_file(outputFile)
        
        if write_success:
            print("File written successfully.")
        else:
            print("Failed to write the file.")
    else:
        print("Failed to read the file.")


except Exception as e:
    print(f"An error occurred: {e}")


