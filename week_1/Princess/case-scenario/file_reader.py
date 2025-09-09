import os
import sys
import pandas as pd

#[START] - Class Body
class file_reader:
    #--------------------------------------------------------------------------------------
    # Initialize all variables used in the class
    #--------------------------------------------------------------------------------------
    
    def __init__(self, file_path=r"C:\\Users\\GW433QS\\OneDrive - EY\Attachments\\Desktop\\Phyton Training\\Week1\\PythonTraining.xlsx"):
        self.file_path = file_path
        self.success = False
        self.content = None

    #Methods
    def read_file(self):
        self.success = True
        try:
            # Simulate file reading logic here
            # Read the 'Employee' sheet
            self.content = pd.read_excel(self.file_path, sheet_name='Employee')
            print(self.content)
            return True
            pass
        except Exception as e:
            self.success = False
            print(f"An error occurred while reading the file: {e}")
            
        return self.success        

    #Properties Get
    def get_content(self):
        return self.content

    

#[END] - Class Body