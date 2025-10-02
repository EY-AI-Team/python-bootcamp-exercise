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
    def validate_phone_number(phone):
        pattern = r'^\d{3}-\d{3}-\d{4}$' # Matches XXX-XXX-XXXX
        return bool(re.match(pattern, phone))

    def process_rows(rows):
        # Example: Process each row
        countRow = 0
        for row in rows:
            countRow = countRow + 1
            if countRow != 1 :
                if validate_phone_number(row[5].strip()) == False: # Output: True
                    print("Invalid Phone Number")
                    logging.debug(f"Invalid Phone Number in line  {countRow} ")
                else:
                    print("Valid Phone number")

except Exception as e:
            messagebox.showerror("Error", str(e))    

