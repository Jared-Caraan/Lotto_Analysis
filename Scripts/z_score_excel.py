import pandas as pd
import numpy as np

from config import filename_excel, filename_z_score

def z_score(df):
    cols = ['first','second','third','fourth','fifth','sixth']
    
    for i in cols:
        cols_zscore = i + '_zscore'
        df[cols_zscore] = (df[i] - df[i].mean()) / df[i].std()

def main():
    
    df = pd.read_excel(filename_excel)
    df.drop(columns=['Unnamed: 0'], inplace=True)
    
    df['Date'] = pd.to_datetime(df['Date'], format = '%d/%m/%Y')
    df['Day_Name'] = df['Date'].dt.day_name()

    z_score(df)
    
    df.to_excel(filename_z_score)
    
if __name__ == "__main__":
    main()