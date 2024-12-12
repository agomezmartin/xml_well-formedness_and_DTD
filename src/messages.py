# src/messages.py

# UI Strings
SELECT_DIRECTORY = "Select a directory containing XML files."
SELECT_LOG_DIRECTORY = "Select directory to save the log file."
LOG_HEADER = "XML Validation Results"
LOG_TIMESTAMP = "Timestamp: {}"
LOG_SEPARATOR = "-" * 40
NO_XML_FILES_FOUND = "No XML files found in the selected directory."
LOG_SAVED = "Results saved to log file: "
LOG_FILE_ERROR = "Error writing to log file: "
VALIDATED_FILE = "Validated file: {}"
RESULT_SUCCESS = "Validation successful."
RESULT_FAILURE = "Validation failed."
ERROR_MESSAGE = "Error: {}"
PARSE_ERROR = "Parse error: {}"

# Well-formedness Validation messages
WELL_FORMED_VALID = "The XML file is well-formed: {}"
WELL_FORMED_INVALID = "The XML file is not well-formed: {}"

# DTD/XSD Validation messages
DTD_XSD_FILE_ERROR = "Error validating XML file against DTD/XSD: {}"
DTD_XSD_VALID = "The XML file is valid against DTD/XSD: {}"
DTD_XSD_INVALID = "The XML file is not valid against DTD/XSD: {}"
