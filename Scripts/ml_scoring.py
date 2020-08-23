import logging
import sys
import numpy as np
import pandas as pd
import joblib

from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from config import filename_odd_even, score_log, test_size, rand_state, pickle_dir

## LOGGER CONFIG
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler(score_log)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def main():
    
    args = sys.argv
    
    input_date = datetime.strptime(args[1], '%m/%d/%Y')
    print(input_date.month)
    #Loading dataset
    # try:
        # df = pd.read_excel(filename_odd_even)
    # except Exception as e:
        # logger.critical("Exception: " + str(e))
    # else:
        # logger.debug("Reading raw data")
    
    #Dropping columns
    # df.drop(columns=['Unnamed: 0', 'Winning Numbers', 'Odd_Even'], inplace=True)
    # logger.debug("Dropped columns")
    
    #Adding features
    # df['Date'] = pd.to_datetime(df['Date'], format = '%d/%m/%Y')
    # df['Day_Name'] = df['Date'].dt.day_name()
    # df['Month_Num'] = df['Date'].dt.month
    # df['Year'] = df['Date'].dt.year
    # logger.debug("Added features")
    
    #Rearranging columns
    # df = df[['Date', 'Day_Name', 'Month_Num', 'Year', 'Odd_Even_Dist']]
    
    #Factorizing categorical value
    # factor_label = pd.factorize(df['Odd_Even_Dist'])
    # df.Odd_Even_Dist = factor_label[0]
    # definitions = factor_label[1]
    
    # factor_day = pd.factorize(df['Day_Name'])
    # df.Day_Name = factor_day[0]
    
    # factor_year = pd.factorize(df['Year'])
    # df.Year = factor_year[0]
    # logger.debug("Factorizing columns")
    
    #Split into dependent and independent variables
    # X = df.iloc[:,1:4].values
    # y = df.iloc[:,4].values
    # logger.debug("Splitting feature and label")
    
    #Train and Test data
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size, random_state = rand_state)
    # logger.debug("Creating train and test data")
    
    #Feature scaling
    # scaler = StandardScaler()
    # X_train = scaler.fit_transform(X_train)
    # print(type(X_test))
    # print(X_test)
    # X_test = scaler.transform(X_test)

if __name__ == "__main__":
    main()