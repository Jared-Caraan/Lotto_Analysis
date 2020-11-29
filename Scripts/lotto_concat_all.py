import pandas as pd

from config import filename_excel, filename_1995, filename_2005, filename_all

def main():
    
    df1 = pd.read_excel(filename_excel)
    df2 = pd.read_excel(filename_2005)
    df3 = pd.read_excel(filename_1995)
    
    final_df = pd.concat([df1,df2,df3]).drop_duplicates().reset_index(drop=True)
    
    final_df.to_excel(filename_all, index = False)

if __name__ == "__main__":
	main()