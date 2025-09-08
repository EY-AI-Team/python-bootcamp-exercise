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
    def read_excel(self, file_path="C:\\Users\\JV833VJ\\OneDrive - EY\\Documents\\Python Lessons\\PythonTraining.xlsx", sheet_name="Employee"):
        self.success = True
        try:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            self.content = df
            print(f"Excel file '{file_path}' read successfully.")
        except Exception as e:
            self.success = False
            print(f"An error occurred while reading the file: {e}")
            
        return self.success        

    #Properties Get
    def get_content(self):
        return self.content;

    

#[END] - Class Body