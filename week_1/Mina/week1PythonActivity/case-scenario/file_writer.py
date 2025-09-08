import os
import sys
import json
import datetime

class file_writer:
    def __init__(self, content):
        self.success = False
        self.content = self._convert_datetimes(content)

    def _convert_datetimes(self, data):
        if isinstance(data, list):
            return [self._convert_datetimes(item) for item in data]
        elif isinstance(data, dict):
            return {key: self._convert_datetimes(value) for key, value in data.items()}
        elif isinstance(data, (datetime.datetime, datetime.date)):
            return data.isoformat()
        else:
            return data

    def write_to_file(self, file_path: str):
        success = True
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(self.content, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")
            success = False
        return success

#[END] - Class Body