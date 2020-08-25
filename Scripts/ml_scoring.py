import logging
import sys
import numpy as np
import pandas as pd
import joblib

from datetime import datetime
from sklearn.preprocessing import StandardScaler
from config import filename_odd_even, score_log, pickle_dir, scaler_dir

## LOGGER CONFIG
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler(score_log)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def main():
    
    open = []
    
    try:
        args = sys.argv
    except Exception as e:
        logger.critical("Exception: " + str(e))
    
    input_date = datetime.strptime(args[1], '%m/%d/%Y')
    open.append(input_date.weekday())
    open.append(input_date.month)
    open.append(0)
    
    arr = np.array(open).reshape(1,3)
    
    ##Load scaler
    try:
        scaler = joblib.load(scaler_dir)
    except Exception as e:
        logger.critical("Exception: " + str(e))
    else:
        logger.debug("Loading scaler")
        
    ##Load model
    try:
        model = joblib.load(pickle_dir)
    except Exception as e:
        logger.critical("Exception: " + str(e))
    else:
        logger.debug("Loading model")
    
    ## Scale input
    X_input = scaler.transform(arr)
    logger.debug("Scaling input")
    
    ## Predict using model
    pred = model.predict(X_input)
    pred_prob = model.predict_proba(X_input)
    logger.debug("Predicted class: " + str(pred))

if __name__ == "__main__":
    main()