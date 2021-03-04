import pandas as pd
import logging
import numpy as np

from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from mlxtend.evaluate import bias_variance_decomp
from config import *

## LOGGER CONFIG
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler(train_log)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def train(df, col, scaler_, model):
    
    #Split into dependent and independent variables
    X = df.iloc[:,0:2].values 
    y = df.iloc[:,2].values
    
    #Train and Test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size, random_state = rand_state)
   
    #Feature scaling
    scaler  = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test  = scaler.transform(X_test)
    
    #Training model
    classifier = RandomForestClassifier()
    clf = RandomizedSearchCV(classifier, model_params, n_iter = 100, cv = 5, random_state = 1)
    
    #Estimate bias, variance, loss
    try:
        loss, bias, var = bias_variance_decomp(clf, X_train, y_train, X_test, y_test, num_rounds=200, random_seed=1)
    except Exception as e:
        logger.critical("Exception: " + str(e))
    else:
        logger.debug("Loss: %.3f" % loss)
        logger.debug("Bias: %.3f" % bias)
        logger.debug("Variance: %.3f" % var)
    
def main():
    
    logger.debug("Generating scaler and model for the six columns")
    
    for i in range(0,1):
        
        #Loading dataset
        try:
            df = pd.read_excel(filename_all)
        except Exception as e:
            logger.critical("Exception: " + str(e))
        
        df = df[['Date', col_list[i]]]
        
        
        #Adding features
        df['Date']  = pd.to_datetime(df['Date'], format = '%d/%m/%Y')
        df['Month']  = df['Date'].dt.strftime('%m')
        df['Day'] = df['Date'].dt.strftime('%d')
        df['Week']  = df['Date'].dt.isocalendar().week
        df['Day'] = df['Day'].apply(lambda x: int(x))
        
        df['week_cos'] = np.cos(2 * np.pi * df['Week'] / 7)
        df['week_sin'] = np.sin(2 * np.pi * df['Week'] / 7)
        
        df['day_cos'] = np.cos(2 * np.pi * df['Day'] / 31)
        df['day_sin'] = np.sin(2 * np.pi * df['Day'] / 31)
        
        # df['month_cos'] = np.cos(2 * np.pi * df['Month'] / 12)
        # df['month_sin'] = np.sin(2 * np.pi * df['Month'] / 12)
        
        #Factorizing categorical value
        logger.debug("Column: " + str(col_list[i]))
        
        df = df[['week_cos', 'week_sin', col_list[i]]]
        
        train(df, str(col_list[i]), scaler_num, model_num)

if __name__ == "__main__":
    main()