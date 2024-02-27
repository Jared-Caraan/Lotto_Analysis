import pandas as pd
import logging

from config import filename_all, delta_log

#Logger Configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler(delta_log)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def main():
    logger.debug("Hello World")
    try:
        df_results = pd.read_excel(filename_all)
    except Exception as e:
        logger.error("Exception: " + str(e))
    else:
        logger.debug("Reading historical data")