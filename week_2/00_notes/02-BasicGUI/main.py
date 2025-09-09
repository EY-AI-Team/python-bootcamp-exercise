import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv

class MainForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CSV Table Viewer")
        self.geometry("800x400")

        self.load_btn = ttk.Button(self, text="Load CSV", command=self.load_csv)
        self.load_btn.pack(pady=10)

        self.table = ttk.Treeview(self)
        self.table.pack(expand=True, fill='both')

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return

        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                rows = list(reader)
                if not rows:
                    messagebox.showerror("Error", "CSV file is empty.")
                    return

                # Clear previous table
                for col in self.table.get_children():
                    self.table.delete(col)
                self.table["columns"] = []
                self.table["show"] = "headings"

                # Set headers
                headers = rows[0]
                self.table["columns"] = headers
                for h in headers:
                    self.table.heading(h, text=h)
                    self.table.column(h, width=100)

                # Insert rows
                for row in rows[1:]:
                    self.table.insert("", "end", values=row)
        
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = MainForm()
    app.mainloop()