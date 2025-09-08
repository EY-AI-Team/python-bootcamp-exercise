import os
import sys
import pandas as pd
import json

#[START] - Class Body
class file_writer:
    #--------------------------------------------------------------------------------------
    # Initialize all variables used in the class
    #--------------------------------------------------------------------------------------
    def __init__(self, content):
        self.success = False
        self.content = content
    

    def write_to_file(self,file_path: str):
        self.success = True
        try:
            # Simulate file writing logic here'
            # Convert to JSON
                  
            json_data = self.content.to_dict(orient='records')
            
            with open(file_path, 'w', encoding='utf-8') as json_file:
                        json.dump(json_data, json_file, ensure_ascii=False, indent=4)
            print(f"Data successfully written to {file_path}")
            
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")
            self.success = False
        return self.success
    #Properties Get
    def get_wheel_count(self):
        return self.wheel_count
    

#[END] - Class Body