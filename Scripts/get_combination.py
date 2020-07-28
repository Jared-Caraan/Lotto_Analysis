import pandas as pd
import numpy as np
import operator

from config import filename_excel

def get_combi(df):
    last_prob = 0.0
    num_col = ['first','second','third', 'fourth', 'fifth', 'sixth']
    num_high = []
    probs = {}
    
    if df.iloc[0].Day_Name == 'Saturday':
        next_day = 'Tuesday'
    elif df.iloc[0].Day_Name == 'Tuesday':
        next_day = 'Thursday'
    else:
        next_day = 'Saturday'
    
    filt = df['Day_Name'] == next_day
    df_filtered = df[filt]
    
    print("For " + next_day + " results")
    for i in num_col:
        
        num_list = list(df_filtered[i].unique())
        print(i)
        for j in num_list:
            
            count = round((((df_filtered[i].values == j).sum()) / len(df_filtered)),2)
            probs[j] = count
            
        num_high.append(max(probs.items(), key=operator.itemgetter(1))[0])
        last_prob = max(probs.items(), key=operator.itemgetter(1))[1]
        print(last_prob)
        probs = {}
            
    return num_high

def main():
    
    df = pd.read_excel(filename_excel)

    df.drop(columns=['Unnamed: 0'], inplace=True)

    df['Date'] = pd.to_datetime(df['Date'], format = '%d/%m/%Y')
    df['Day_Name'] = df['Date'].dt.day_name()
    
    print(get_combi(df))

if __name__ == "__main__":
    main()