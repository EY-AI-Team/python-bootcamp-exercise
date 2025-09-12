import logging
import os

def setup_logging(log_file='execution.log'):
    logging.basicConfig(
        filename=os.path.abspath(log_file),
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )