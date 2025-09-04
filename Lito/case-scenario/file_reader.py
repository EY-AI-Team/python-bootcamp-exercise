from pathlib import Path
import pandas as panda

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
            excel_filepath: str = f"{Path(__file__).parent}/pythonbootcamp.xlsx"
            excel_data = panda.read_excel(excel_filepath)
            data_list = excel_data.to_dict(orient='records')
            for data in data_list:
                print(data)
            self.content = data_list
            
        except Exception as e:
            self.success = False
            print(f"An error occurred while reading the file: {e}")
            
        return self.success

    #Properties Get
    def get_content(self):
        return self.content;

    

#[END] - Class Body