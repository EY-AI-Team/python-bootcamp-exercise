import tkinter as tk
#https://docs.python.org/3/library/tkinter.html

from tkinter import ttk, filedialog, messagebox
import re
import logging
#Import logging configuration
from logging_config import setup_logging

#Setup logging
setup_logging()
try:
    def process_rows(rows):
        # Example: Process each row
        countRow = 0
        for row in rows:
            countRow = countRow + 1
            if countRow != 1 :
                if isinstance(int(row[0]), int) == False: # Output: True
                    print("Invalid Employee ID")
                    logging.debug(f"Invalid Employee ID in line {countRow}")
                else:
                    print("Valid Employee ID")

except Exception as e:
            messagebox.showerror("Error", str(e))    

