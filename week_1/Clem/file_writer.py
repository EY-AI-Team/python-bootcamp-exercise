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
    

    def write_to_file(self,file_path: str):       
        try:
            # Simulate file writing logic here
             with open(file_path, "w") as writer:
                writer.write(self.content)
                self.success = True
                pass      
       
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")
            self.success= False
    
        return self.success

    #Properties Get
    def get_wheel_count(self):
        return self.wheel_count;
    

#[END] - Class Body