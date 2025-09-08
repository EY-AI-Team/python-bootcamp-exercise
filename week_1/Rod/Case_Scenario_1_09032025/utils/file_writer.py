# Import standard and third-party libraries
import pandas as pd  # For reading Excel and CSV files
import json  # For writing JSON output
import math  # For checking NaN values
from datetime import datetime  # For formatting datetime objects
from pathlib import Path  # For handling file paths
from dotenv import load_dotenv  # For loading environment variables from a .env file

# Load environment variables from .env file
load_dotenv()

# Class responsible for cleaning and writing data to a JSON file
class JsonWriter:
    def __init__(self, output_path: Path):
        self.output_path = output_path

    # Method to clean data before writing to JSON
    def data_cleaner(self, data: list[dict]) -> list[dict]:
        for record in data:
            for key, value in record.items():
                # Replace None or NaN values with None
                if value is None or (isinstance(value, float) and math.isnan(value)):
                    record[key] = None
                # Strip whitespace from string values
                elif isinstance(value, str):
                    record[key] = value.strip()
                # Format datetime objects to YYYY-MM-DD
                elif isinstance(value, (pd.Timestamp, datetime)):
                    record[key] = value.strftime("%Y-%m-%d")
                # Ensure all values are JSON serializable
                else:
                    try:
                        json.dumps(value)
                    except TypeError:
                        # Convert non-serializable objects to strings
                        record[key] = str(value)
        return data
    # Method to write cleaned data to a JSON file
    def write_json(self, data: list[dict]):
        clean_data = self.data_cleaner(data)

        try:
            # Create output directory if it doesn't exist
            self.output_path.parent.mkdir(parents=True, exist_ok=True)

            # Write data to JSON file with indentation
            with open(self.output_path, "w", encoding="utf-8") as f:
                json.dump(clean_data, f, indent=4)
        except Exception as e:
            # Raise a runtime error if writing fails
            raise RuntimeError(f"Failed to write JSON file: {e}") from e