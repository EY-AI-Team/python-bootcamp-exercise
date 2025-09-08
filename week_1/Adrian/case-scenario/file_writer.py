import os
import json

#[START] - Class Body
class file_writer:
    #--------------------------------------------------------------------------------------
    # Initialize all variables used in the class
    #--------------------------------------------------------------------------------------
    def __init__(self, content):
        self.success = False
        self.content = content

    def write_to_file(self, file_path: str):
        self.success = True
        try:
            # Convert DataFrame to JSON string
            json_data = self.content.to_json(orient='records', indent=4)
            # Write JSON string to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(json_data)
            return True
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")
            self.success = False
            return False

    #Properties Get
    # Remove get_wheel_count if not needed
#[END] - Class Body