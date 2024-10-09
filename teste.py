import tkinter as tk
from tkinter import filedialog
import pyperclip

def select_file():
    # Open a file dialog to select a file
    file_path = filedialog.askopenfilename()
    if file_path:
        # Copy the file path to the clipboard
        pyperclip.copy(file_path)
        print(f"Copied path: {file_path}")

# Set up the main application window
root = tk.Tk()
root.title("File Path Copier")

# Create a button to open the file dialog
button = tk.Button(root, text="Select a File", command=select_file)
button.pack(pady=20)

# Run the application
root.mainloop()
