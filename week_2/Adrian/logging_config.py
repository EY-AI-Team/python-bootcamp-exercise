#https://docs.python.org/3/library/logging.html#logging-levels
import logging

def setup_logging():
    logging.basicConfig(
        filename= r'C:\Users\MV268SE\Repos\python-bootcamp-exercise\week_2\Adrian\Logs\test.log',
        level=logging.WARNING,  # Set the logging level to WARNING
        format='%(asctime)s - %(levelname)s - %(message)s'
    )