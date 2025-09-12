#!/usr/bin/env python3
"""
Tkinter Form with Right-Aligned Buttons

This script creates a simple form using tkinter with two buttons aligned to the right side.
Includes example form fields and proper button alignment techniques.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys

class FormWithRightButtons:
    """
    A class to create a form with right-aligned buttons using tkinter
    """
    
    def __init__(self):
        """Initialize the form"""
        self.root = tk.Tk()
        self.setup_window()
        self.create_form()
        self.create_buttons()
    
    def setup_window(self):
        """Configure the main window"""
        self.root.title("Form with Right-Aligned Buttons")
        self.root.geometry("400x300")
        self.root.resizable(True, True)
        
        # Center the window on screen
        self.center_window()
        
        # Configure the main container
        self.root.configure(bg='#f0f0f0')
    
    def center_window(self):
        """Center the window on the screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_form(self):
        """Create the form fields"""
        # Main form frame
        self.form_frame = ttk.Frame(self.root, padding="20")
        self.form_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(
            self.form_frame, 
            text="Sample Form", 
            font=('Arial', 16, 'bold')
        )
        title_label.pack(pady=(0, 20))
        
        # Name field
        name_frame = ttk.Frame(self.form_frame)
        name_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(name_frame, text="Name:", width=12).pack(side=tk.LEFT)
        self.name_entry = ttk.Entry(name_frame, width=30)
        self.name_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Email field
        email_frame = ttk.Frame(self.form_frame)
        email_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(email_frame, text="Email:", width=12).pack(side=tk.LEFT)
        self.email_entry = ttk.Entry(email_frame, width=30)
        self.email_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Phone field
        phone_frame = ttk.Frame(self.form_frame)
        phone_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(phone_frame, text="Phone:", width=12).pack(side=tk.LEFT)
        self.phone_entry = ttk.Entry(phone_frame, width=30)
        self.phone_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Comments field
        comments_frame = ttk.Frame(self.form_frame)
        comments_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        ttk.Label(comments_frame, text="Comments:").pack(anchor=tk.W)
        self.comments_text = tk.Text(
            comments_frame, 
            height=5, 
            wrap=tk.WORD,
            font=('Arial', 10)
        )
        self.comments_text.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        
        # Add scrollbar to text widget
        scrollbar = ttk.Scrollbar(comments_frame, orient=tk.VERTICAL, command=self.comments_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.comments_text.configure(yscrollcommand=scrollbar.set)
    
    def create_buttons(self):
        """Create the right-aligned buttons"""
        # Button frame - this is key for right alignment
        button_frame = ttk.Frame(self.form_frame)
        button_frame.pack(fill=tk.X, pady=(10, 0))
        
        # Method 1: Using pack with side=tk.RIGHT (buttons appear in reverse order)
        self.cancel_button = ttk.Button(
            button_frame,
            text="Cancel",
            command=self.on_cancel,
            width=10
        )
        self.cancel_button.pack(side=tk.RIGHT, padx=(10, 0))
        
        self.submit_button = ttk.Button(
            button_frame,
            text="Submit",
            command=self.on_submit,
            width=10
        )
        self.submit_button.pack(side=tk.RIGHT)
        
        # Alternative Method 2: Using grid for more control
        # Uncomment the code below and comment out the pack method above to use grid
        
        # # Configure grid weights to push buttons to the right
        # button_frame.columnconfigure(0, weight=1)  # Empty space takes all extra space
        # button_frame.columnconfigure(1, weight=0)  # Submit button column
        # button_frame.columnconfigure(2, weight=0)  # Cancel button column
        # 
        # self.submit_button = ttk.Button(
        #     button_frame,
        #     text="Submit",
        #     command=self.on_submit,
        #     width=10
        # )
        # self.submit_button.grid(row=0, column=1, padx=(0, 10), sticky=tk.E)
        # 
        # self.cancel_button = ttk.Button(
        #     button_frame,
        #     text="Cancel",
        #     command=self.on_cancel,
        #     width=10
        # )
        # self.cancel_button.grid(row=0, column=2, sticky=tk.E)
    
    def on_submit(self):
        """Handle submit button click"""
        # Get form data
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()
        comments = self.comments_text.get("1.0", tk.END).strip()
        
        # Simple validation
        if not name:
            messagebox.showerror("Error", "Please enter your name")
            self.name_entry.focus()
            return
        
        if not email:
            messagebox.showerror("Error", "Please enter your email")
            self.email_entry.focus()
            return
        
        # Display submitted data
        form_data = f"""Form Submitted Successfully!
        
Name: {name}
Email: {email}
Phone: {phone}
Comments: {comments}"""
        
        messagebox.showinfo("Form Submitted", form_data)
        
        # Optional: Clear form after submission
        self.clear_form()
    
    def on_cancel(self):
        """Handle cancel button click"""
        # Ask for confirmation
        if messagebox.askyesno("Confirm", "Are you sure you want to cancel?"):
            self.clear_form()
    
    def clear_form(self):
        """Clear all form fields"""
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.comments_text.delete("1.0", tk.END)
        self.name_entry.focus()
    
    def run(self):
        """Start the GUI application"""
        # Set focus to first field
        self.name_entry.focus()
        
        # Start the main event loop
        self.root.mainloop()


# Alternative simpler version for just the buttons
class SimpleRightAlignedButtons:
    """
    Simplified version focusing only on right-aligned buttons
    """
    
    def __init__(self):
        self.root = tk.Tk()
        self.setup_simple_form()
    
    def setup_simple_form(self):
        """Create a simple form with right-aligned buttons"""
        self.root.title("Simple Right-Aligned Buttons")
        self.root.geometry("300x200")
        self.root.configure(bg='white')
        
        # Main content area
        content_frame = ttk.Frame(self.root, padding="20")
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Some sample content
        ttk.Label(content_frame, text="Sample Form Content", font=('Arial', 12)).pack(pady=20)
        ttk.Entry(content_frame, width=30).pack(pady=10)
        
        # Button container frame
        button_frame = ttk.Frame(content_frame)
        button_frame.pack(fill=tk.X, pady=(20, 0))
        
        # Right-aligned buttons using pack
        ttk.Button(button_frame, text="Cancel", width=10).pack(side=tk.RIGHT, padx=(10, 0))
        ttk.Button(button_frame, text="OK", width=10).pack(side=tk.RIGHT)
    
    def run(self):
        self.root.mainloop()


# Example with different button alignment methods
class ButtonAlignmentExamples:
    """
    Show different ways to align buttons to the right
    """
    
    def __init__(self):
        self.root = tk.Tk()
        self.setup_examples()
    
    def setup_examples(self):
        """Create examples of different alignment methods"""
        self.root.title("Button Alignment Examples")
        self.root.geometry("400x400")
        
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Example 1: Using pack with side=RIGHT
        ttk.Label(main_frame, text="Method 1: pack(side=tk.RIGHT)", font=('Arial', 10, 'bold')).pack(anchor=tk.W, pady=(0, 5))
        
        frame1 = ttk.Frame(main_frame, relief=tk.RIDGE, borderwidth=1, padding="10")
        frame1.pack(fill=tk.X, pady=(0, 20))
        
        btn_frame1 = ttk.Frame(frame1)
        btn_frame1.pack(fill=tk.X)
        
        ttk.Button(btn_frame1, text="Cancel").pack(side=tk.RIGHT, padx=(10, 0))
        ttk.Button(btn_frame1, text="OK").pack(side=tk.RIGHT)
        
        # Example 2: Using grid
        ttk.Label(main_frame, text="Method 2: grid with sticky=E", font=('Arial', 10, 'bold')).pack(anchor=tk.W, pady=(0, 5))
        
        frame2 = ttk.Frame(main_frame, relief=tk.RIDGE, borderwidth=1, padding="10")
        frame2.pack(fill=tk.X, pady=(0, 20))
        
        frame2.columnconfigure(0, weight=1)
        ttk.Button(frame2, text="OK").grid(row=0, column=1, padx=(0, 10))
        ttk.Button(frame2, text="Cancel").grid(row=0, column=2)
        
        # Example 3: Using anchor
        ttk.Label(main_frame, text="Method 3: pack with anchor=E", font=('Arial', 10, 'bold')).pack(anchor=tk.W, pady=(0, 5))
        
        frame3 = ttk.Frame(main_frame, relief=tk.RIDGE, borderwidth=1, padding="10")
        frame3.pack(fill=tk.X)
        
        btn_container = ttk.Frame(frame3)
        btn_container.pack(anchor=tk.E)
        
        ttk.Button(btn_container, text="OK").pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(btn_container, text="Cancel").pack(side=tk.LEFT)
    
    def run(self):
        self.root.mainloop()


def main():
    """Main function to run the application"""
    if len(sys.argv) > 1:
        if sys.argv[1] == "--simple":
            print("Running simple version...")
            app = SimpleRightAlignedButtons()
        elif sys.argv[1] == "--examples":
            print("Running alignment examples...")
            app = ButtonAlignmentExamples()
        else:
            print("Unknown argument. Running default version...")
            app = FormWithRightButtons()
    else:
        print("Running full form version...")
        print("Use --simple for simple version or --examples for alignment examples")
        app = FormWithRightButtons()
    
    try:
        app.run()
    except KeyboardInterrupt:
        print("\nApplication closed by user")
    except Exception as e:
        print(f"Error running application: {e}")


if __name__ == "__main__":
    main()


# Additional utility functions for button alignment
def create_right_aligned_buttons(parent, button_configs):
    """
    Utility function to create right-aligned buttons
    
    Args:
        parent: Parent widget
        button_configs: List of dictionaries with button configuration
                       [{"text": "OK", "command": callback}, {"text": "Cancel", "command": callback2}]
    
    Returns:
        List of button widgets
    """
    button_frame = ttk.Frame(parent)
    button_frame.pack(fill=tk.X, pady=(10, 0))
    
    buttons = []
    
    # Create buttons in reverse order for pack(side=tk.RIGHT)
    for config in reversed(button_configs):
        btn = ttk.Button(
            button_frame,
            text=config.get("text", "Button"),
            command=config.get("command", lambda: None),
            width=config.get("width", 10)
        )
        
        if len(buttons) == 0:  # First button (rightmost)
            btn.pack(side=tk.RIGHT)
        else:  # Subsequent buttons
            btn.pack(side=tk.RIGHT, padx=(10, 0))
        
        buttons.append(btn)
    
    return buttons


# Usage example:
"""
# Basic usage
app = FormWithRightButtons()
app.run()

# Simple version
app = SimpleRightAlignedButtons()
app.run()

# Examples of different alignment methods
app = ButtonAlignmentExamples()
app.run()

# Using the utility function
def my_submit():
    print("Submit clicked")

def my_cancel():
    print("Cancel clicked")

root = tk.Tk()
frame = ttk.Frame(root, padding="20")
frame.pack()

button_configs = [
    {"text": "Submit", "command": my_submit},
    {"text": "Cancel", "command": my_cancel}
]

buttons = create_right_aligned_buttons(frame, button_configs)
root.mainloop()
"""