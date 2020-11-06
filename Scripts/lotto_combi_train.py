import logging
import numpy as np
import pandas as pd
import joblib

from pprint import pprint
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import confusion_matrix, accuracy_score
from config import *

## LOGGER CONFIG
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler(train_log)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def train(df, col, label, scaler_, model):
    
    #Split into dependent and independent variables
    X = df.iloc[:,0:2].values 
    y = df.iloc[:,2].values
    logger.debug("Splitting feature and label")
    
    #Train and Test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size, random_state = rand_state)
    logger.debug("Creating train and test data")
   
    #Feature scaling
    scaler  = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test  = scaler.transform(X_test)
    logger.debug("Performing scaling")
    
    #Training model
    classifier = RandomForestClassifier()
    clf = RandomizedSearchCV(classifier, model_params, n_iter = 100, cv = 5, random_state = 1)
    clf.fit(X_train, y_train)
    logger.debug("Training")
    
    #Predicting the test set
    y_pred = clf.predict(X_test)
    logger.debug("Predicting test set")
    
    #Reverse factorize
    reversefactor = dict(zip(range(len(label)), label))
    y_test        = np.vectorize(reversefactor.get)(y_test)
    y_pred        = np.vectorize(reversefactor.get)(y_pred)
    logger.debug(reversefactor)
    
    #Metrics
    try:
        logger.debug("Accuracy = {0:.2f}".format(accuracy_score(y_test,y_pred) * 100))
    except Exception as e:
        logger.critical("Exception: " + str(e))
    
    scaler_ = scaler_ + "_{}.pkl".format(col)
    model   = model + "_{}.pkl".format(col)
    
    #Saving the scaler
    try:
        joblib.dump(scaler, scaler_)
    except Exception as e:
        logger.critical("Exception: " + str(e))
    else:
        logger.debug("Saving scaler")
    
    #Saving the model
    try:
        joblib.dump(clf, model)
    except Exception as e:
        logger.critical("Exception: " + str(e))
    else:
        logger.debug("Saving model")

def main():
    
    logger.debug("Generating scaler and model for the six columns")
    
    for i in range(len(col_list)):
        
        #Loading dataset
        try:
            df = pd.read_excel(filename_all)
        except Exception as e:
            logger.critical("Exception: " + str(e))
        else:
            logger.debug("Reading raw data")
        
        #Adding features
        df['Date']      = pd.to_datetime(df['Date'], format = '%d/%m/%Y')
        df['Day_Num']   = df['Date'].dt.weekday
        df['Year']      = df['Date'].dt.year
        
        logger.debug("Added features")
        
        df = df[['Day_Num', 'Year', col_list[i]]]
        
        #Factorizing categorical value
        logger.debug("Column: " + str(col_list[i]))
        logger.debug(df.head())
        label_list = sorted(df[col_list[i]].unique())
        logger.debug("Label list: " + str(label_list))
        
        factor_list = list(np.arange(0,len(label_list)))
        df.loc[:,col_list[i]] = df.loc[:,col_list[i]].replace(label_list, factor_list)
    
        factor_year = pd.factorize(df['Year'])
        df.Year     = factor_year[0]
        
        logger.debug("Factorizing columns")
        logger.debug(df.head())
        
        train(df, str(col_list[i]), label_list, scaler_num, model_num)

if __name__ == "__main__":
    main()