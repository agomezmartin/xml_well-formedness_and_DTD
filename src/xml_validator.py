# src/xml_validator.py
import os
import xml.etree.ElementTree as ET
from lxml import etree
from . import messages
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to validate XML well-formedness
def validate_xml(file_path, well_formed_only=True, dtd_xsd_file=None):
    if well_formed_only:
        try:
            tree = ET.parse(file_path)
            return True, messages.WELL_FORMED_VALID.format(os.path.basename(file_path))
        except ET.ParseError as e:
            return False, messages.WELL_FORMED_INVALID.format(os.path.basename(file_path)) + f"\n{messages.PARSE_ERROR.format(e)}"
    else:
        try:
            # Validate against DTD/XSD using lxml
            tree = etree.parse(file_path)
            if dtd_xsd_file.endswith(".xsd"):
                schema = etree.XMLSchema(file=dtd_xsd_file)  # Load XSD
                schema.assertValid(tree)  # Validate against XSD
                return True, messages.DTD_XSD_VALID.format(os.path.basename(file_path))
            elif dtd_xsd_file.endswith(".dtd"):
                dtd = etree.DTD(dtd_xsd_file)  # Load DTD
                if not dtd.validate(tree):
                    return False, messages.DTD_XSD_INVALID.format(os.path.basename(file_path)) + f"\n{dtd.error_log}"
            return True, messages.DTD_XSD_VALID.format(os.path.basename(file_path))
        except etree.XMLSchemaParseError as e:
            return False, messages.DTD_XSD_FILE_ERROR.format(e)
        except etree.DTDParseError as e:
            return False, messages.DTD_XSD_FILE_ERROR.format(e)
        except etree.DocumentInvalid as e:
            return False, messages.DTD_XSD_INVALID.format(os.path.basename(file_path)) + f"\n{messages.PARSE_ERROR.format(e)}"

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

# Function to validate all XML files in a given directory and log the results
def validate_all_xml_files(directory, log_file, well_formed_only=True, dtd_xsd_file=None):
    try:
        with open(log_file, 'a') as log:
            log.write(f"{messages.LOG_HEADER} {directory}\n")
            log.write(messages.LOG_TIMESTAMP.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "\n")
            log.write(messages.LOG_SEPARATOR + "\n")
            
            # Get all XML files in the directory
            xml_files = [f for f in os.listdir(directory) if f.lower().endswith(".xml")]
            
            if not xml_files:
                return messages.NO_XML_FILES_FOUND
            
            # Loop through each XML file and validate
            for xml_file in xml_files:
                file_path = os.path.join(directory, xml_file)
                result, message = validate_xml(file_path, well_formed_only, dtd_xsd_file)
                log.write(f"{messages.VALIDATED_FILE.format(os.path.basename(file_path))}\n")
                log.write(f"{messages.RESULT_SUCCESS if result else messages.RESULT_FAILURE}\n")
                log.write(f"{messages.ERROR_MESSAGE.format(message)}\n")
                log.write(messages.LOG_SEPARATOR + "\n")
            
            return messages.LOG_SAVED + log_file
    except Exception as e:
        return messages.LOG_FILE_ERROR + str(e)

# GUI functions for the application

# Function to create and show the GUI
def create_gui():
    # Create the main window
    root = tk.Tk()
    root.title("XML Validator with Log")
    root.geometry("400x300")  # Width x Height

    def validate_well_formed():
        directory = select_directory(filedialog)
        if directory:
            log_file = save_log_path(filedialog)
            if log_file:
                result = validate_all_xml_files(directory, log_file, well_formed_only=True)
                messagebox.showinfo("Log Saved", result)
    
    def validate_with_dtd_xsd():
        directory = select_directory(filedialog)
        if directory:
            log_file = save_log_path(filedialog)
            if log_file:
                dtd_xsd_file = filedialog.askopenfilename(title="Select DTD/XSD File", filetypes=[("XML Schema", "*.xsd"), ("DTD File", "*.dtd")])
                if dtd_xsd_file:
                    result = validate_all_xml_files(directory, log_file, well_formed_only=False, dtd_xsd_file=dtd_xsd_file)
                    messagebox.showinfo("Log Saved", result)

    # Add a button to validate well-formed XML files
    validate_well_formed_button = tk.Button(root, text="Validate Well-Formed XML", command=validate_well_formed)
    validate_well_formed_button.pack(pady=20)

    # Add a button to validate XML files against a DTD/XSD file
    validate_dtd_xsd_button = tk.Button(root, text="Validate XML with DTD/XSD", command=validate_with_dtd_xsd)
    validate_dtd_xsd_button.pack(pady=20)

    # Run the application
    root.mainloop()

# Function to start the application
def run_gui():
    create_gui()
