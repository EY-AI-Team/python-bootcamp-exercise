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
    def is_valid_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def process_rows(rows):
        # Example: Process each row
        countRow = 0
        for row in rows:
            countRow = countRow + 1
            if countRow != 1 :
                print("Valid email" if is_valid_email(row[3]) else "Invalid email")
                logging.debug(f"Valid email" if is_valid_email(row[3]) else "Invalid email {countRow}")
except Exception as e:
        messagebox.showerror("error", str(e))

