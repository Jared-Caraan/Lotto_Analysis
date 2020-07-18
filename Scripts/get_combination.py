import pandas as pd
import numpy as np

from config import filename_excel

def get_combi(df):
    num_col = ['first']
    probs = {}
    
    if df.iloc[0].Day_Name == 'Saturday':
        next_day = 'Tuesday'
    elif df.iloc[0].Day_Name == 'Tuesday':
        next_day = 'Thursday'
    else:
        next_day = 'Saturday'
    
    filt = df['Day_Name'] == next_day
    df_filtered = df[filt]
    
    for i in num_col:
        num_list = list(df_filtered[i].unique())
        for j in num_list:
            count = ((df_filtered[i].values == j).sum()) / len(df_filtered)
            print(count)
            probs[j] = count
            
    return probs

def main():
    
    df = pd.read_excel(filename_excel)

    df.drop(columns=['Unnamed: 0'], inplace=True)

    df['Date'] = pd.to_datetime(df['Date'], format = '%d/%m/%Y')
    df['Day_Name'] = df['Date'].dt.day_name()
    
    print(get_combi(df))

if __name__ == "__main__":
    main()