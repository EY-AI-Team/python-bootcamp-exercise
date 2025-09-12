import os
import logging
import pandas as pd
import re
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from loader import load_csv_with_validation

# Setup logging
logging.basicConfig(
    filename='execution.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def validate_row(row):
    errors = []
    if len(row) != 12:
        errors.append("Row does not have 12 columns.")
    if any(str(cell).strip() == "" for cell in row):
        errors.append("Empty string in one or more columns.")
    try:
        int(row[0])
    except:
        errors.append("Employee ID is not an integer.")
    # Basic email validation
    if "@" not in row[4] or "." not in row[4]:
        errors.append("Invalid email address.")
    # Phone number validation: ###-###-####
    if not re.match(r"\d{3}-\d{3}-\d{4}$", row[5]):
        errors.append("Invalid phone number format.")
    return errors

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee CSV Loader")
        self.data = None
        self.header = None

        # Table
        self.table = ttk.Treeview(root)
        self.table.pack(expand=True, fill='both', padx=10, pady=10)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(fill='x', padx=10, pady=5)

        self.load_btn = tk.Button(btn_frame, text="Load", command=self.load_csv)
        self.load_btn.pack(side='left', padx=5)

        self.save_btn = tk.Button(btn_frame, text="Save", command=self.save_excel, state='disabled')
        self.save_btn.pack(side='left', padx=5)

    def load_csv(self):
        file_path = filedialog.askopenfilename(
            title="Select CSV File",
            filetypes=[("CSV Files", "*.csv")]
        )
        if not file_path:
            return

        try:
            header, valid_rows, errors = load_csv_with_validation(file_path, validate_row)
        except Exception as e:
            logging.error(f"Exception during loading: {e}")
            messagebox.showerror("Error", str(e))
            return

        # Log errors
        for line_num, row, errs in errors:
            logging.error(f"Line {line_num}: {errs} | Data: {row}")

        if not valid_rows:
            self.data = None
            self.header = None
            self.save_btn.config(state='disabled')
            self.clear_table()
            messagebox.showwarning("No valid data", "No valid rows found in the file.")
            return

        self.data = pd.DataFrame(valid_rows, columns=header)
        self.header = header
        self.populate_table(header, valid_rows)
        self.save_btn.config(state='normal')

    def save_excel(self):
        if self.data is None or self.header is None:
            return

        save_path = filedialog.asksaveasfilename(
            title="Save Excel File",
            defaultextension=".xlsx",
            filetypes=[("Excel Files", "*.xlsx")]
        )
        if not save_path:
            return

        try:
            self.data.to_excel(save_path, index=False)
            messagebox.showinfo("Success", f"File saved to {save_path}")
        except Exception as e:
            logging.error(f"Exception during saving: {e}")
            messagebox.showerror("Error", str(e))

    def populate_table(self, header, rows):
        self.clear_table()
        self.table["columns"] = header
        self.table["show"] = "headings"
        for col in header:
            self.table.heading(col, text=col)
            self.table.column(col, width=100, anchor='center')
        for row in rows:
            self.table.insert("", "end", values=row)

    def clear_table(self):
        for item in self.table.get_children():
            self.table.delete(item)
        self.table["columns"] = []
        self.table["show"] = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()