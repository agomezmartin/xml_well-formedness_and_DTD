import tkinter as tk
from tkinter import filedialog, messagebox
from .xml_validator import validate_all_xml_files
from . import messages

# Function to allow the user to select the directory containing XML files
def select_directory(filedialog):
    directory = filedialog.askdirectory(title=messages.SELECT_DIRECTORY)
    return directory

# Function to allow the user to select the path to save the log
def save_log_path(filedialog):
    log_dir = filedialog.askdirectory(title=messages.SELECT_LOG_DIRECTORY)
    if log_dir:
        log_filename = filedialog.asksaveasfilename(initialdir=log_dir, defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        return log_filename
    return None

# Function to validate XML files in a given directory and log the results
def validate_well_formed():
    directory = select_directory(filedialog)
    if directory:
        log_file = save_log_path(filedialog)
        if log_file:
            result = validate_all_xml_files(directory, log_file, well_formed_only=True)
            messagebox.showinfo(messages.LOG_SAVED_WINDOW_TITLE, result)

# Function to validate XML files with DTD/XSD
def validate_with_dtd_xsd():
    directory = select_directory(filedialog)
    if directory:
        log_file = save_log_path(filedialog)
        if log_file:
            dtd_xsd_file = filedialog.askopenfilename(title=messages.SELECT_DTD_XSD_FILE, filetypes=[("XML Schema", "*.xsd"), ("DTD File", "*.dtd")])
            if dtd_xsd_file:
                result = validate_all_xml_files(directory, log_file, well_formed_only=False, dtd_xsd_file=dtd_xsd_file)
                messagebox.showinfo(messages.LOG_SAVED_WINDOW_TITLE, result)

# Function to create and show the GUI
def create_gui():
    # Create the main window
    root = tk.Tk()
    root.title(messages.MAIN_WINDOW_TITLE)
    root.geometry("400x300")  # Width x Height

    # Add a button to validate well-formed XML files
    validate_well_formed_button = tk.Button(root, text=messages.WELL_FORMED_BUTTON_TEXT, command=validate_well_formed)
    validate_well_formed_button.pack(pady=20)

    # Add a button to validate XML files against a DTD/XSD file
    validate_dtd_xsd_button = tk.Button(root, text=messages.VALIDATE_DTD_XSD_BUTTON_TEXT, command=validate_with_dtd_xsd)
    validate_dtd_xsd_button.pack(pady=20)

    # Run the application
    root.mainloop()

# Function to start the application
def run_gui():
    create_gui()
