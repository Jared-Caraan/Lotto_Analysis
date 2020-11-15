import logging
import sys
import numpy as np
import pandas as pd
import joblib

from datetime import datetime
from sklearn.preprocessing import StandardScaler
from config import score_log, model_num, scaler_num, col_list

## LOGGER CONFIG
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler(score_log)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def score(arr, col, scaler_, model_):
    
    scaler_  = scaler_ + "_{}.pkl".format(col)
    model_   = model_ + "_{}.pkl".format(col)
    
    ##Load scaler
    try:
        scaler = joblib.load(scaler_)
    except Exception as e:
        logger.critical("Exception: " + str(e))
    else:
        logger.debug("Loading scaler")
        
    ##Load model
    try:
        model = joblib.load(model_)
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
    
    return str(pred)

def main():
    
    open      = []
    pred_list = []
    
    try:
        args = sys.argv
    except Exception as e:
        logger.critical("Exception: " + str(e))
    
    input_date = datetime.strptime(args[1], '%m/%d/%Y')
    open.append(input_date.strftime("%m"))
    open.append(input_date.strftime("%W"))
    
    arr = np.array(open).reshape(1,2)
    
    for i in range(len(col_list)):
        logger.debug("Predicting " + col_list[i] )
        
        pred_num = score(arr, col_list[i], scaler_num, model_num)
        pred_list.append(pred_num)
    
    logger.debug(pred_list)

if __name__ == "__main__":
    main()