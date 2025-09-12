import os
import csv
import logging
import tkinter as tk
import pandas as pd

from tkinter import filedialog

#[START] - Class Body
class DataSave_EXCEL:
    #--------------------------------------------------------------------------------------
    # Initialize all variables used in the class
    #--------------------------------------------------------------------------------------
    def __init__(self, dataset):
        logging.debug("Initialize FileLoader Object")
        self.dataset = dataset

    #--------------------------------------------------------------------------------------
    # Save data to Excel file
    #--------------------------------------------------------------------------------------
    def save_excel(self):
        if not self.dataset or len(self.dataset) < 2:
            logging.error("No data available to save.")
            raise ValueError("No data available to save.")

        df = pd.DataFrame(self.dataset[1:], columns=self.dataset[0])
        
        try:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".xlsx",  # Default file extension
                filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")], # Filter file types
                title="Save File"
                )
            
            df.to_excel(file_path, index=False)
            logging.info(f"Data successfully saved to Excel file: {file_path}")
        
        except Exception as e:
            logging.error(f"Failed to save data to Excel file: {e}")
            raise e