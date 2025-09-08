import os
import sys

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
            import pandas as pd
            if isinstance(self.content, pd.DataFrame):
                self.content.to_json(file_path, orient='records', indent=4)
            else:
                print("Content is not a pandas DataFrame.")
                success = False
        except Exception as e:
            import traceback
            print(f"An error occurred while writing to the file: {e}")
            traceback.print_exc()
            success = False
        return success

    #Properties Get
    def get_wheel_count(self):
        return self.wheel_count;
    

#[END] - Class Body