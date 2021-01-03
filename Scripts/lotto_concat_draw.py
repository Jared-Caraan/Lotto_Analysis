import pandas as pd

from config import filename_excel, filename_2005, filename_1995, filename_all, ref_draw

def main():

    df = pd.read_excel(filename_excel)
    df2 = pd.read_excel(filename_2005)
    df3 = pd.read_excel(filename_1995)

    final_df = pd.concat([df,df2]).drop_duplicates().reset_index(drop=True)
    
    checkpoint = final_df[final_df['Date'] == '2011-07-23'].index[0]
    
    final_df.insert(0, 'Draw', range(checkpoint + ref_draw, ((checkpoint + ref_draw)-len(final_df)), -1))
    
    df3.sort_values(by = 'Date', ascending = False, inplace = True)
    
    df3.insert(0, 'Draw', range(len(df3), 0, -1))
    
    new_df = pd.concat([final_df,df3]).drop_duplicates().reset_index(drop=True)
    
    new_df.to_excel(filename_all, index = False)
    

if __name__ == "__main__":
    main()