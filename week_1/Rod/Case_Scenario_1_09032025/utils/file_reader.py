# Import standard and third-party libraries
import os
import pandas as pd  # For reading Excel and CSV files
import ast  # For safely evaluating string representations of Python literals
from pathlib import Path  # For handling file paths
from dotenv import load_dotenv  # For loading environment variables from a .env file

# Load environment variables from .env file
load_dotenv()

# Class responsible for reading input files
class FileReader:
    def __init__(self, file_path: Path):
        self.file_path = file_path

        # Load supported formats from environment variable and convert to list
        formats_str = os.getenv("SUPPORTED_FORMATS")
        self.SUPPORTED_FORMATS = ast.literal_eval(formats_str)

        # Load sheet name for Excel files from environment variable
        self.sheet_name = os.getenv("SHEET_NAME")

    # Method to read data from the file and return a list of dictionaries
    def read(self) -> list[dict]:
        # Check if the file exists
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")

        # Check if the file format is supported
        if self.file_path.suffix not in self.SUPPORTED_FORMATS:
            raise ValueError(
                f"Unsupported file format '{self.file_path.suffix}'. "
                f"Supported formats are: {', '.join(self.SUPPORTED_FORMATS)}"
            )

        try:
            # Read Excel or CSV file based on file extension
            if self.file_path.suffix in [".xlsx", ".xls"]:
                df = pd.read_excel(self.file_path, sheet_name=self.sheet_name)
            elif self.file_path.suffix == ".csv":
                df = pd.read_csv(self.file_path)

            # Raise error if the file is empty
            if df.empty:
                raise ValueError("Input file is empty.")

            # Convert DataFrame to list of dictionaries
            return df.to_dict(orient="records")

        except Exception as e:
            # Raise a runtime error with the original exception
            raise RuntimeError(f"Failed to read file: {e}") from e
