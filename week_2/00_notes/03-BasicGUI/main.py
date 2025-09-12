import tkinter as tk
#https://docs.python.org/3/library/tkinter.html

from tkinter import ttk, filedialog, messagebox
import csv
import re
import openpyxl  # You need to install this with `pip install openpyxl`
import pandas as pd
import logging

#Import logging configuration
from logging_config import setup_logging

setup_logging()
logging.info("Logging initialized successfully.")

class MainForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CSV Table Viewer")
        self.geometry("800x400")

        self.load_btn = ttk.Button(self, text="Load", command=self.load_csv)
        self.load_btn.pack(pady=10)

        # Save button, initially disabled
        self.save_btn = ttk.Button(self, text="Save", command=self.save_to_excel, state=tk.DISABLED)
        self.save_btn.pack(pady=10)

        self.table = ttk.Treeview(self)
        self.table.pack(expand=True, fill='both')

    def is_valid_email(self, email):
        # Basic email regex
        return re.match(r".*@[a-zA-Z]*\.com", email)

    def is_valid_phone(self, phone):
        return re.match(r"^\d{3}-\d{3}-\d{4}$", phone)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return

        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                rows = list(reader)

                if not rows:
                    raise Exception("CSV file is empty.")

                headers = rows[0]

               
                # Clear previous table
                for col in self.table.get_children():
                    self.table.delete(col)
                self.table["columns"] = []
                self.table["show"] = "headings"

                self.table["columns"] = headers
                for h in headers:
                    self.table.heading(h, text=h)
                    self.table.column(h, width=100)

                
                try:
                    int(headers[0])
                    # If this conversion works, first row might be data, so no header
                    logging.error(f"CSV file does not have a header row.")
                    messagebox.showerror("Error", str("CSV file does not have a header row."))
                except Exception:
                    # If conversion fails, it's likely a header (string column names)
                    pass


                 # Validate header
                if len(headers) != 12:
                    raise Exception("CSV header must have exactly 12 columns.")


                enable_save_btn = True
                 # Insert rows
                for row in rows[1:]:
                    
                    if len(row) != 12:
                        logging.error(f"Line {rows.index(row)+1}: Invalid column count")

                    for col in row:
                        if col.strip() == "":
                            logging.error(f"Line {rows.index(row)+1}: Empty string found in row")
                            enable_save_btn = False
                            #break

                        if row.index(col) == 0:  # Employee ID
                            try:
                                int(col)
                            except ValueError:
                                logging.error(f"Line {rows.index(row)+1}: Employee ID is not an integer")
                                enable_save_btn = False
                                #break

                        if row.index(col) == 3:  # Email at column 3
                            if not self.is_valid_email(col):
                                logging.error(f"Line {rows.index(row)+1}: Invalid email format")
                                enable_save_btn = False
                                #break

                        if row.index(col) == 4:  # Phone at column 4
                            if not self.is_valid_phone(col):
                                logging.error(f"Line {rows.index(row)+1}: Invalid phone number format")
                                enable_save_btn = False
                                #break
                    if enable_save_btn:
                        self.save_btn.config(state=tk.NORMAL)
                    else:
                        self.save_btn.config(state=tk.DISABLED)
                    self.table.insert("", "end", values=row)

        except Exception as e:
            logging.exception("Failed to load CSV file")
            messagebox.showerror("Error", str(e))

    def save_to_excel(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if not file_path:
            return

        try:
            # Extract headers
            headers = self.table["columns"]

            # Extract all row data
            data = []
            for item in self.table.get_children():
                values = self.table.item(item)["values"]
                data.append(values)

            # Create DataFrame and write to Excel
            df = pd.DataFrame(data, columns=headers)
            df.to_excel(file_path, index=False)

            messagebox.showinfo("Success", "Table saved to Excel successfully.")
        except Exception as e:
            logging.exception("Failed to save Excel file using pandas")
            messagebox.showerror("Error", f"Failed to save Excel file: {str(e)}")

if __name__ == "__main__": 
    app = MainForm()
    app.mainloop()
    
