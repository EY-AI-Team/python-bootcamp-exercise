import sys
import os
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
    def read_file(self,file_path):
        self.success = True
        self.file_path=file_path
        try:
            # Simulate file reading logic here
            df = pd.read_excel(self.file_path,sheet_name=1)            
            self.content =  df.to_json(orient="records", indent=4)
            pass
        
        except Exception as e:
            self.success = False
            print(f"An error occurred while reading the file: {e}")
            
        return self.success        

    #Properties Get
    def get_content(self):
        return self.content;

    

#[END] - Class Body