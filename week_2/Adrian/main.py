import tkinter as tk
import logging

from tkinter import ttk, filedialog
from Model.DataLoad_CSV import DataLoad_CSV
from Model.DataSave_EXCEL import DataSave_EXCEL
from logging_config import setup_logging

#Setup logging
setup_logging()

class EmployeeDisplay(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CSV Table Viewer")
        self.geometry("800x400")

        # Futuristic button frame
        button_frame = tk.Frame(self, bg="#181A20", bd=3, relief="ridge", highlightbackground="#00FFF7", highlightthickness=2)
        button_frame.pack(fill=tk.X, pady=(10, 0))

        # Custom style for buttons
        style = ttk.Style()
        style.configure("Futuristic.TButton", foreground="#00FFF7", background="#181A20", font=("Segoe UI", 12, "bold"))

        self.load_btn = ttk.Button(button_frame, text="Open", command=self.load_csv, style="Futuristic.TButton")
        self.load_btn.pack(side=tk.RIGHT, padx=(10, 0))

        self.save_btn = ttk.Button(button_frame, text="Save", command=self.save_csv, state=tk.DISABLED, style="Futuristic.TButton")
        self.save_btn.pack(side=tk.RIGHT)

        self.table = ttk.Treeview(self)
        self.table.pack(expand=True, fill='both')

    def load_csv(self):
        try:
            self.fl = DataLoad_CSV()
            self.fl.load_csv()
            self.fl.validate()
            valid_data = self.fl.get_data()

            if len(valid_data) > 0:
                self.save_btn.config(state=tk.ACTIVE)

            # Clear previous table
            for col in self.table.get_children():
                self.table.delete(col)
            self.table["columns"] = []
            self.table["show"] = "headings"

            # Set headers
            headers = valid_data[0]
            self.table["columns"] = headers
            for h in headers:
                self.table.heading(h, text=h)
                self.table.column(h, width=100)

            # Insert rows
            for row in valid_data[1:]:
                self.table.insert("", "end", values=row)
        
        except Exception as e:
            logging.error(str(e))

    def save_csv(self):
        try:
            logging.info("Save button clicked")
            exportdata = DataSave_EXCEL(self.fl.get_data())
            exportdata.save_excel()
            
        except Exception as e:
            logging.error(str(e))

if __name__ == "__main__":
    app = EmployeeDisplay()
    app.mainloop()