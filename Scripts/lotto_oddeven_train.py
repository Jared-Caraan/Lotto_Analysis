import logging
import numpy as np
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from config import filename_excel, train_log, test_size, rand_state, n_estimators, criterion, pickle_odd_even, scaler_odd_even

## LOGGER CONFIG
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler(train_log)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def factorize(row):
    
    if row == "Even: 0, Odd: 6":
        return 0
    elif row == "Even: 1, Odd: 5":
        return 1
    elif row == "Even: 2, Odd: 4":
        return 2
    elif row == "Even: 3, Odd: 3":
        return 3
    elif row == "Even: 4, Odd: 2":
        return 4
    elif row == "Even: 5, Odd: 1":
        return 5
    else:
        return 6

def main():
    
    ##Loading dataset
    try:
        df = pd.read_excel(filename_excel)
    except Exception as e:
        logger.critical("Exception: " + str(e))
    else:
        logger.debug("Reading raw data")
    
    ##Dropping columns
    df.drop(columns=['Unnamed: 0', 'Winning Numbers', 'Odd_Even', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'Day_Name'], inplace=True)
    logger.debug("Dropped columns")
    
    ##Adding features
    df['Date'] = pd.to_datetime(df['Date'], format = '%d/%m/%Y')
    df['Day_Num'] = df['Date'].dt.weekday
    df['Month_Num'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year
    logger.debug("Added features")
    
    ##Rearranging columns
    df = df[['Date', 'Day_Num', 'Month_Num', 'Year', 'Odd_Even_Dist']]
    
    ##Factorizing categorical value
    label_list = sorted(df['Odd_Even_Dist'].unique())
    
    df['Odd_Even_Dist'] = df['Odd_Even_Dist'].apply(lambda x: factorize(str(x)))
    
    factor_year = pd.factorize(df['Year'])
    df.Year = factor_year[0]
    logger.debug("Factorizing columns")
    
    ##Split into dependent and independent variables
    X = df.iloc[:,1:4].values 
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
    
    ##Reverse factorize
    reversefactor = dict(zip(range(8), label_list))
    y_test = np.vectorize(reversefactor.get)(y_test)
    y_pred = np.vectorize(reversefactor.get)(y_pred)
    
    ##Confusion Matrix
    print(pd.crosstab(y_test, y_pred, rownames = ['Actual Pattern'], colnames = ['Predicted Pattern']))
    
    ##Saving the scaler
    try:
        joblib.dump(scaler, scaler_odd_even)
    except Exception as e:
        logger.critical("Exception: " + str(e))
    else:
        logger.debug("Saving scaler")
    
    ##Saving the model
    try:
        joblib.dump(classifier, pickle_odd_even)
    except Exception as e:
        logger.critical("Exception: " + str(e))
    else:
        logger.debug("Saving model")

if __name__ == "__main__":
    main()