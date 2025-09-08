from xslxtojson import xslxtojson
from pathlib import Path

class main:

    def __init__(self):
        self.excel_filepath: str = 'C:/Users/UA149NV/source/repos/python-bootcamp-exercise/Lito/pythonbootcamp.xlsx'
        self.json_filepath: str = 'C:/Users/UA149NV/source/repos/python-bootcamp-exercise/Lito/output.json'
        self.executexslstojson()

    def executexslstojson(self):
        # Initialize xslxtojson
        myxslxtojson = xslxtojson()
        # Read Excel file and convert it to a list
        data_list = myxslxtojson.read_exceltolist(self.excel_filepath)
        if data_list != None:
            # Display Data
            for data in data_list:
                print(data)
            # Convert list to json
            if myxslxtojson.write_listtojson(self.json_filepath, data_list) == True:
                print(f"{self.json_filepath} has been created.")
            else:
                print(f"Failed to create {self.json_filepath}.")
        else:
            print(f"Failed to read {self.excel_filepath}")

if __name__ == "__main__":
    main_instance = main()