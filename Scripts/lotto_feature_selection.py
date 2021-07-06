import pandas as pd
import numpy as np

from sklearn.feature_selection import SelectKBest, f_classif, f_regression
from config import filename_excel

def main():

    #Loading dataset
    df = pd.read_excel(filename_excel)
    
    #Adding Columns
    df['Date']      = pd.to_datetime(df['Date'], format = '%d/%m/%Y')
    df['Day_Num']   = df['Date'].dt.weekday
    df['Month_Num'] = df['Date'].dt.month
    df['Year']      = df['Date'].dt.year
    df['Week']      = df['Date'].dt.strftime('%V')
    
    week_int = pd.to_numeric(df['Week'])
    df.Week  = week_int
    
    df = df[['Day_Num', 'Month_Num', 'Year', 'Week', 'first']]
    
    factor_year = pd.factorize(df['Year'])
    df.Year = factor_year[0]
    
    label_list        = sorted(df['first'].unique())
    factor_list       = list(np.arange(0,len(label_list)))
    df.loc[:,'first'] = df.loc[:,'first'].replace(label_list, factor_list)
    
    #Split into dependent and independent variables
    X = df.iloc[:,0:4].values
    y = df.iloc[:,4].values
    
    X_new = SelectKBest(score_func = f_regression, k=2).fit_transform(X,y)
    print(df.head())
    print(X_new[:4])

if __name__ == "__main__":
	main()