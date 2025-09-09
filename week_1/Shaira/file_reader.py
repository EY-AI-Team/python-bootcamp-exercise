import os
import sys
import pandas as pd

#[START] - Class Body
class file_reader_class:
    #--------------------------------------------------------------------------------------
    # Initialize all variables used in the class
    #--------------------------------------------------------------------------------------
    def __init__(self):
        self.success = False;
        self.content = None;

    #Methods
    def read_file(self, filePath, sheetName):
        try:
            # Simulate file reading logic here
            df = pd.read_excel(filePath, sheet_name=sheetName)
            df = df.where(pd.notnull(df), None)
            self.content = df
            self.success = True
            return self.success
           
        except Exception as e:
            self.success = False
            print(f"An error occurred while reading the file: {e}")
            
        return self.success        

    #Properties Get
    def get_content(self):
        return self.content;

    

#[END] - Class Body