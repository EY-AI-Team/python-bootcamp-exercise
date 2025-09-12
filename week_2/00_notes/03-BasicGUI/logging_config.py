import logging

def setup_logging():
    logging.basicConfig(
        filename= r'C:\Users\uf189za\OneDrive - EY\Desktop\Python_Bootcamp\python-bootcamp-exercise\week_2\00_notes\03-BasicGUI\logs\app.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )