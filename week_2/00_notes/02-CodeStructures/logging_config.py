import logging

def setup_logging():
    logging.basicConfig(
        filename= r'C:\Users\AC129VR\OneDrive - EY\Documents\GitHub\python-bootcamp-exercise\week_2\00_notes\02-CodeStructures\app.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )