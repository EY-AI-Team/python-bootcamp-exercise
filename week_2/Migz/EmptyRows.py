import tkinter as tk
import logging
#https://docs.python.org/3/library/tkinter.html

from tkinter import ttk, filedialog, messagebox
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
                x = 0
                while x < 12:
                    if row[x] == "":
                        print("Error", "There is empty in line  # : ")
                        print(countRow)
                        logging.debug(f"There is empty in line  # :  {countRow}")
                
                        x = x + 1
                        continue
                    else:
                        x = x + 1
                        continue
except Exception as e:
            messagebox.showerror("Error", str(e))    