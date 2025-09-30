#https://docs.python.org/3/library/logging.html#logging-levels
import logging

def setup_logging():
    logging.basicConfig(
        filename= r'C:\Users\AC129VR\OneDrive - EY\Documents\GitHub\python-bootcamp-exercise\week_3\00_notes\API\Logs\log.log',
        level=logging.WARNING,  # Set the logging level to WARNING
        format='%(asctime)s - %(levelname)s - %(message)s'
    )