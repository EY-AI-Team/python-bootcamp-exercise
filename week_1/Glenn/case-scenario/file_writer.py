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
    

    def write_to_file(self,filename: str):
        success = True
        try:
            # Simulate file writing logic here
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(self.content)
            self.success = True
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")
            self.success = False

        return self.success
    

#[END] - Class Body