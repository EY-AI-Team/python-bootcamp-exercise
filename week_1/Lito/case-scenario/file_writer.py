import json
import pandas as panda

#[START] - Class Body
class file_writer:
    #--------------------------------------------------------------------------------------
    # Initialize all variables used in the class
    #--------------------------------------------------------------------------------------
    def __init__(self, content):
        self.success = False;
        self.content = content;
    
    def write_to_file(self, file_path: str):
        success = True
        try:
            data_list: list = self.content
            for row in data_list:
                for key, value in row.items():
                    if panda.isna(value):
                        row[key] = None # If NaN, mark them as null/none
                    elif isinstance(value, panda.Timestamp):
                        row[key] = value.strftime('%d-%m-%Y') # If obj timestamp, convert it to a formatted string
                    elif isinstance(value, str):
                        row[key] = value.strip() # Trim string values
            # Serialize List to json
            with open(file_path, 'w') as json_file:
                json.dump(data_list, json_file, indent=4)

        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")
            success = False

        return success

    #Properties Get
    def get_wheel_count(self):
        return self.wheel_count;
    

#[END] - Class Body