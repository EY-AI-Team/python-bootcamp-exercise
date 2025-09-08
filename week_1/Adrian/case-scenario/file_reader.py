import os
import sys
import pandas as pd

#[START] - Class Body
class file_reader:
    #--------------------------------------------------------------------------------------
    # Initialize all variables used in the class
    #--------------------------------------------------------------------------------------
    def __init__(self):
        self.success = False
        self.content = None

    #Methods
    def read_file(self):
        self.success = True
        try:
            self.content = pd.read_excel('C:\\Users\\MV268SE\\Downloads\\PythonTraining.xlsx',sheet_name= "Employee")
            self.success = True
            pass
        except Exception as e:
            self.success = False
            print(f"An error occurred while reading the file: {e}")
            
        return self.success        

    #Properties Get
    def get_content(self):
        return self.content

    

#[END] - Class Body