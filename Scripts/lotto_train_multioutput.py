import logging
import numpy as np
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.multioutput import MultiOutputClassifier
from sklearn.tree import DecisionTreeClassifier, ExtraTreeClassifier
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.neighbors import RadiusNeighborsClassifier, KNeighborsClassifier
from config import *

def main():
    
    # Data
    df = pd.read_excel(filename_all)
    
    # Transformation
    df['Date']  = pd.to_datetime(df['Date'], format = '%d/%m/%Y')
    df['Week']  = df['Date'].dt.isocalendar().week
    df['Month'] = df['Date'].dt.month
    
    df = df[['Week', 'Month', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth']]
    
    factor_week = pd.factorize(df['Week'])
    df.Week     = factor_week[0]
    
    factor_month = pd.factorize(df['Month'])
    df.Month     = factor_month[0]
    
    # Split into dependent and independent variables
    X = df.iloc[:,0:2].values 
    y = np.asarray(df[df.columns[2:]])
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    
    # Scaling
    scaler  = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test  = scaler.transform(X_test)
    
    # Model
    d_tree = ExtraTreesClassifier()
    classifier = MultiOutputClassifier(d_tree)
    classifier.fit(X_train, y_train)
    
    # Score
    y_pred = classifier.predict(X_test)
    print(X_test.shape)
    print(y_pred.shape)
    print(classifier.score(X_test, y_pred))
    
    new = []
    input_date = datetime.strptime('11/10/2020', '%m/%d/%Y')
    new.append(input_date.strftime("%W"))
    new.append(input_date.strftime("%m"))
    
    arr = np.array(new).reshape(1,2)
    scale_arr = scaler.transform(arr)
    
    res = classifier.predict(scale_arr)
    print(res)
    
if __name__ == "__main__":
    main()