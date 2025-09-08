import os
import sys
import pandas as pd
from pathlib import Path

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
            # Simulate file reading logic here

            # Relative Path
            relative_path = Path("data/TestExcelFile.xlsx")
            file_path = Path(__file__).parent/relative_path

            #Read Excel File
            df = pd.read_excel(file_path)
            self.content = df.to_json(orient='records', indent=4)

            self.success = True
            print(f"File read successful")

            pass
        except Exception as e:
            self.success = False
            print(f"An error occurred while reading the file: {e}")
            
        return self.success  

    #Properties Get
    def get_content(self):
        return self.content;

    

#[END] - Class Body