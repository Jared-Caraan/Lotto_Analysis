import pandas as pd

from config import filename_2005

def main():
    
    df = pd.read_excel(filename_2005)
    df.drop(columns = ['Unnamed: 0'], inplace = True)
    
    df['first']  = df['first'].astype(int)
    df['second'] = df['second'].astype(int)
    df['third']  = df['third'].astype(int)
    df['fourth'] = df['fourth'].astype(int)
    df['fifth']  = df['fifth'].astype(int)
    df['sixth']  = df['sixth'].astype(int)
    
    df.to_excel(filename_2005, index = False)

if __name__ == "__main__":
    main()