# Import necessary modules
import os
from pathlib import Path
from dotenv import load_dotenv  # For loading environment variables from a .env file

# Custom utility classes
from utils.file_reader import FileReader
from utils.file_writer import JsonWriter

def main():
    # Load environment variables from .env file
    load_dotenv()

    # Get input and output file paths from environment variables
    input_path = Path(os.getenv("INPUT_FILE_PATH"))
    output_path = Path(os.getenv("OUTPUT_FILE_PATH"))

    # Initialize file reader and writer with the specified paths
    reader = FileReader(input_path)
    writer = JsonWriter(output_path)

    try:
        # Read data from the input file
        print(f"Reading from: {input_path}")
        data = reader.read()

        # Write the data to the output file in JSON format
        print(f"Writing to: {output_path}")
        writer.write_json(data)

        # Confirm successful conversion
        print("Successfully converted to JSON.")
    except Exception as e:
        # Handle any errors that occur during reading or writing
        print(f"Error: {e}")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
