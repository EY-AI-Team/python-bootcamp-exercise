import json

#[START] - Class Body
class file_writer:
    #--------------------------------------------------------------------------------------
    # Initialize all variables used in the class
    #--------------------------------------------------------------------------------------
    def __init__(self, content):
        self.success = False;
        self.content = content; 

    def write_to_file(self,file_path: str):
        self.success = True
        try:
            data = self.content
            if hasattr(data, "to_dict"):
                data = data.to_dict(orient="records")
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4, default=str)
            print(f"Data written to JSON file '{file_path}' successfully.")
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")
            self.success = False
        return self.success

    #Properties Get
    def get_wheel_count(self):
        return self.wheel_count;
    

#[END] - Class Body