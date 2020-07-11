import pandas as pd
import numpy as np

from config import filename_excel, filename_rng_test

d_alpha = 0.565

def kolmogorov_smirnov(rows):
    d_func = []
    d_plus = []
    d_minus = []
    list_num = list(rows.split(","))
    
    for idx in range(0, len(list_num)):
        i = (idx + 1 / len(list_num))
        plus = (i / len(list_num)) - int(list_num[idx])
        minus = int(list_num[idx]) - ((i-1) / len(list_num))
        
        d_plus.append(plus)
        d_minus.append(minus)
    
    d_func.append(max(d_plus))
    d_func.append(max(d_minus))
    
    d_val = max(d_func)
    
    if d_val < d_alpha:
        return "PASS"
    
    return "FAIL"

def main():

    df = pd.read_excel(filename_excel)
    df.drop(columns=['Unnamed: 0', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth'], inplace=True)

    df['Date'] = pd.to_datetime(df['Date'], format = '%d/%m/%Y')

    filt = df['Date'] >= df['Date'].max() - pd.DateOffset(months=6)
    df_year = df[filt]
    df = df_year.copy()
    
    df['Kolmogorov_Smirnov_Test'] = df['Winning Numbers'].apply(lambda x: kolmogorov_smirnov(x))
    
    df.to_excel(filename_rng_test)

if __name__ == "__main__":
    main()