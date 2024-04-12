import logging

def setup_logging():
    # Configure logging settings
    logging.basicConfig(filename='app.log', level=logging.INFO)

def log_info(message):
    # Log an info message
    logging.info(message)

def log_error(message):
    # Log an error message
    logging.error(message)