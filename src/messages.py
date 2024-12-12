# messages.py

# General Messages
LOG_HEADER = "XML Validation Results"
LOG_TIMESTAMP = "Timestamp: {}"
LOG_SEPARATOR = "----------------------------------------"
NO_XML_FILES_FOUND = "No XML files found in the selected directory."
LOG_SAVED = "Results saved to log file: {}"
LOG_FILE_ERROR = "Error writing to log file: {}"
VALIDATED_FILE = "Validated file: {}"
RESULT_SUCCESS = "Validation successful."
RESULT_FAILURE = "Validation failed."
ERROR_MESSAGE = "Error details: {}"

# Schema-Related Messages
SCHEMA_FILE_LOGGED = "Schema File: {}"
DTD_XSD_VALID = "The XML file is valid against the provided DTD/XSD."
DTD_XSD_INVALID = "The XML file is not valid against the provided DTD/XSD."
DTD_XSD_FILE_ERROR = "Error loading the DTD/XSD file: {}"

# Parsing-Related Messages
WELL_FORMED_VALID = "The XML file '{}' is well-formed."
WELL_FORMED_INVALID = "The XML file '{}' is not well-formed."
PARSE_ERROR = "Parse error: {}"

# GUI Messages (Window Titles, Button Text, etc.)
MAIN_WINDOW_TITLE = "XML Validator with Log"
WELL_FORMED_BUTTON_TEXT = "Validate Well-Formed XML"
VALIDATE_DTD_XSD_BUTTON_TEXT = "Validate XML with DTD/XSD"
LOG_SAVED_WINDOW_TITLE = "Log Saved"
SELECT_DIRECTORY = "Select Directory"
SELECT_LOG_DIRECTORY = "Select Log Directory"
SELECT_DTD_XSD_FILE = "Select DTD/XSD File"
ERROR_TITLE = "Error"
INFO_TITLE = "Information"
MISSING_PATHS_ERROR = "Please specify both a directory and a log file path."
TEXT_FILES = "Text Files"
SCHEMA_FILES = "Schema Files (*.dtd, *.xsd)"
