import os
import sys
import pandas as pd

#[START] - Class Body
class file_reader:
    #--------------------------------------------------------------------------------------
    # Initialize all variables used in the class
    #--------------------------------------------------------------------------------------
    def __init__(self):
        self.success = False;
        self.content = None;

    #Methods
    def read_file(self):
        self.success = True
        try:
            self.content = pd.read_excel("PythonTraining_1.xlsx", sheet_name="Employee")
            self.success = True
        except Exception as e:
            self.success = False
            print(f"An error occurred while reading the file: {e}")
            
        return self.success

    def convert_to_json(self):
        
        try:
            self.content = self.content.to_json(orient="records", indent=4)
            self.success = True
            pass
        except Exception as e:
            self.success = False
            print(f"An error occurred while converting data to json: {e}")

        return self.success
    #Properties Get
    def get_content(self):
        return self.content

    

#[END] - Class Body