import logging
import numpy as np
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from config import filename_excel, train_log, test_size, rand_state, n_estimators, criterion, model_num, scaler_num, col_list

## LOGGER CONFIG
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler(train_log)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def train(df, col, label, scaler_, model):
    
    ##Split into dependent and independent variables
    X = df.iloc[:,0:4].values 
    y = df.iloc[:,4].values
    logger.debug("Splitting feature and label")
    
    ##Train and Test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size, random_state = rand_state)
    logger.debug("Creating train and test data")
   
    ##Feature scaling
    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    logger.debug("Performing scaling")
    
    ##Training model
    classifier = RandomForestClassifier(n_estimators = n_estimators, criterion = criterion, random_state = rand_state)
    classifier.fit(X_train, y_train)
    logger.debug("Training")
    
    ##Predicting the test set
    y_pred = classifier.predict(X_test)
    logger.debug("Predicting test set")
    
    ##Reverse factorize
    reversefactor = dict(zip(range(len(label)), label))
    logger.debug(reversefactor)
    y_test = np.vectorize(reversefactor.get)(y_test)
    y_pred = np.vectorize(reversefactor.get)(y_pred)
    
    ##Metrics
    try:
        logger.debug("Accuracy = {0:.2f}".format(accuracy_score(y_test,y_pred) * 100))
    except Exception as e:
        logger.critical("Exception: " + str(e))
    
    scaler_ = scaler_ + "_{}.pkl".format(col)
    model   = model + "_{}.pkl".format(col)
    
    ##Saving the scaler
    try:
        joblib.dump(scaler, scaler_)
    except Exception as e:
        logger.critical("Exception: " + str(e))
    else:
        logger.debug("Saving scaler")
    
    ##Saving the model
    try:
        joblib.dump(classifier, model)
    except Exception as e:
        logger.critical("Exception: " + str(e))
    else:
        logger.debug("Saving model")

def main():
    
    logger.debug("Generating scaler and model for the six columns")
    
    for i in range(len(col_list)):
        
        ##Loading dataset
        try:
            df = pd.read_excel(filename_excel)
        except Exception as e:
            logger.critical("Exception: " + str(e))
        else:
            logger.debug("Reading raw data")
        
        ##Adding features
        df['Date'] = pd.to_datetime(df['Date'], format = '%d/%m/%Y')
        df['Day_Num'] = df['Date'].dt.weekday
        df['Month_Num'] = df['Date'].dt.month
        df['Year'] = df['Date'].dt.year
        df['Week'] = df['Date'].dt.strftime('%V')
        week_int = pd.to_numeric(df['Week'])
        df.Week = week_int
        logger.debug("Added features")
        
        df = df[['Day_Num', 'Month_Num', 'Year', 'Week', col_list[i]]]
        
        ##Factorizing categorical value
        logger.debug("Column: " + str(col_list[i]))
        logger.debug(df.head())
        label_list = sorted(df[col_list[i]].unique())
        logger.debug("Label list: " + str(label_list))
        
        factor_list = list(np.arange(0,len(label_list)))
        df.loc[:,col_list[i]] = df.loc[:,col_list[i]].replace(label_list, factor_list)
    
        factor_year = pd.factorize(df['Year'])
        df.Year = factor_year[0]
        logger.debug("Factorizing columns")
        logger.debug(df.head())
        
        train(df, str(col_list[i]), label_list, scaler_num, model_num)

if __name__ == "__main__":
    main()