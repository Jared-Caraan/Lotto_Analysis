import logging
import numpy as np
import pandas as pd
import joblib

from scipy import stats
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from pprint import pprint
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
    X = df.iloc[:,0:1].values 
    y = df.iloc[:,1].values
    
    #Train and Test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size, random_state = rand_state)
   
    #Feature scaling
    scaler  = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test  = scaler.transform(X_test)
    
    #Training model
    classifier = RandomForestClassifier()
    clf = RandomizedSearchCV(classifier, model_params, n_iter = 100, cv = 5, random_state = 1)
    clf.fit(X_train, y_train)
    
    #Predicting the test set
    y_pred = clf.predict(X_test)
    
    #Reverse factorize
    reversefactor = dict(zip(range(len(label)), label))
    y_test        = np.vectorize(reversefactor.get)(y_test)
    y_pred        = np.vectorize(reversefactor.get)(y_pred)
    logger.debug(reversefactor)
    
    #Metrics
    try:
        logger.debug("Accuracy = {0:.2f}".format(accuracy_score(y_test,y_pred) * 100))
        logger.debug("Precision = {0:.2f}".format(precision_score(y_test,y_pred) * 100))
        logger.debug("Recall = {0:.2f}".format(recall_score(y_test,y_pred) * 100))
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
        
        df = df[['Date', col_list[i]]]
        
        #Adding features
        df['Date']  = pd.to_datetime(df['Date'], format = '%d/%m/%Y')
        df['Year']  = df['Date'].dt.year
        df['Month'] = df['Date'].dt.month
        df['Week']  = df['Date'].dt.isocalendar().week
        df['Day']   = df['Date'].dt.day
        df['Dweek'] = df['Date'].dt.dayofweek
        
        
        
        #Factorizing categorical value
        logger.debug("Column: " + str(col_list[i]))
        logger.debug(df.head())
        label_list = sorted(df[col_list[i]].unique())
        
        factor_list = list(np.arange(0,len(label_list)))
        df.loc[:,col_list[i]] = df.loc[:,col_list[i]].replace(label_list, factor_list)
        
        corr_df = df.corr()[[col_list[i]]].sort_values(by=col_list[i], ascending=False)
        ind     = corr_df.iloc[[1]].index.to_numpy()[0]
        
        print(ind)
        df = df[[ind, col_list[i]]]
        
        print(df.head())
        # factor_month = pd.factorize(df['Month'])
        # df.Month     = factor_month[0]
        
        # factor_week = pd.factorize(df['Week'])
        # df.Week     = factor_week[0]

        # logger.debug(df.head())
        
        # train(df, str(col_list[i]), label_list, scaler_num, model_num)

if __name__ == "__main__":
    main()