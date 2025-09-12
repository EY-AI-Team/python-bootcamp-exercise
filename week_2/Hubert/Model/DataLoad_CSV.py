import os
import csv
import logging

from Validator.DataValidator import DataValidator

#[START] - Class Body
class DataLoad_CSV:
    #--------------------------------------------------------------------------------------
    # Initialize all variables used in the class
    #--------------------------------------------------------------------------------------
    def __init__(self, file_path):
        logging.debug("Initialize FileLoader Object")
        self.file_path = file_path
        self.dataset_raw = []
        self.dataset_valid = []

    
    #--------------------------------------------------------------------------------------
    # Validate individual data fields
    #--------------------------------------------------------------------------------------
    def load_csv(self):
        if not os.path.isfile(self.file_path):
            logging.error(f"File not found: {self.file_path}")
            raise FileNotFoundError(f"File not found: {self.file_path}")

        with open(self.file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            self.dataset_raw = list(reader)
            if not self.dataset_raw:
                logging.error("CSV file is empty.")
                raise ValueError("CSV file is empty.")
            
            logging.info(f"Successfully loaded CSV file: {self.file_path}")
    
    #--------------------------------------------------------------------------------------
    # Validate individual data fields
    #--------------------------------------------------------------------------------------
    def validate(self):
        # Example validation: Check if all rows have the same number of columns as the header
        header_length = len(self.dataset_raw[0])
        self.dataset_valid.append(self.dataset_raw[0])  # Always include header
        
        for i, row in enumerate(self.dataset_raw[1:], start=2):
            if len(row) != header_length:
                logging.error(f"Row {i} has an incorrect number of columns.")

            validator = DataValidator(row, i)
            
            if validator.IsValid():
                self.dataset_valid.append(row)
                

        logging.info("CSV data validation successful.")
        return True


    #--------------------------------------------------------------------------------------    # Get loaded data
    #--------------------------------------------------------------------------------------
    def get_data(self):
        if len(self.dataset_valid) == 0:
            logging.error("Data not loaded. Please load and validate the CSV file first.")
        
        return self.dataset_valid