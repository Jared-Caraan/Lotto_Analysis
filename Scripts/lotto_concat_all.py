import pandas as pd

from config import filename_excel, filename_1995, filename_2005, filename_all

def main():
    
    df1 = pd.read_excel(filename_excel)
    df2 = pd.read_excel(filename_2005)
    
    df1.drop(columns = ['Unnamed: 0'], inplace = True)
    df2.drop(columns = ['Unnamed: 0'], inplace = True)
    
    final_df = pd.concat([df1,df2]).drop_duplicates().reset_index(drop=True)
    
    final_df.to_excel(filename_all)

if __name__ == "__main__":
	main()