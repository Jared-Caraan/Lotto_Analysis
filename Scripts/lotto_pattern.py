import pandas as pd

from config import filename_excel, filename_odd_even

def odd_even(x):

     pattern_str = list(x.split(","))
     
     pattern_list = []
     res = "-"
     
     for i in pattern_str:
        if int(i.lstrip('0')) % 2 == 0:
            pattern_list.append("even")
        else:
            pattern_list.append("odd")
     
     return (res.join(pattern_list))
        
def main():
    
    df = pd.read_excel(filename_excel)
    df.drop(columns=['Unnamed: 0', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth'], inplace=True)
    
    df['Date'] = pd.to_datetime(df['Date'], format = '%d/%m/%Y')
    df['Day_Name'] = df['Date'].dt.day_name()

    df['Odd_Even'] = df['Winning Numbers'].apply(lambda x: odd_even(str(x)))
    
    df.to_excel(filename_odd_even)

if __name__ == "__main__":
    main()