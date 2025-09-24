import logging

def setup_logging():
    logging.basicConfig(
        filename= r'C:\Users\CS158EW\OneDrive - EY\Desktop\Python Training\python-bootcamp-exercise\week_2\Migz\logs.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )