import pandas as pd
import requests
import logging

from bs4 import BeautifulSoup
from config import scrape_log, first_batch, col_list, filename_1995

##Logger Configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler(scrape_log)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def extract(a):
    
    a = str(a).replace("<td>", "")
    a = str(a).replace ("</td>", "")
    a = str(a).strip()
    
    return a

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
     
def odd_even_dist(x):
    
    pattern_str = list(x.split("-"))
    
    even_count = 0
    odd_count = 0
    
    for i in pattern_str:
        if i == 'even':
            even_count += 1
        else:
            odd_count += 1
            
    return "Even: {}, Odd: {}".format(str(even_count), str(odd_count))
    
def join(df):
    
    return df['col1'] + ',' + df['col2'] + ',' + df['col3'] + ',' + df['col4'] + ',' + df['col5'] + ',' +  df['col6']

def main():

    #Create new dataframe
    df = pd.DataFrame()
    
    try:
        response = requests.get(first_batch)
    except Exception as e:
        logger.error("Exception: " + str(e))
        
    #Parsing the html structure
    soup = BeautifulSoup(response.text, "html.parser")
    
    row = soup.findAll('td')
    
    logger.debug("Extracting dates and numbers")
    for i in range(0,7):
        row_info = row[i::7]
        row_extract = map(extract,row_info)
        df['col' + str(i)] = list(row_extract)
    
    #Adding columns
    logger.debug("Adding extra columns")
    df['col0']     = pd.to_datetime(df['col0'], format = '%m/%d/%Y')
    df['Day_Name'] = df['col0'].dt.day_name()
    
    df['Winning Numbers'] = df.apply(join, axis=1)
    df['Odd_Even']        = df['Winning Numbers'].apply(lambda x: odd_even(x))
    df['Odd_Even_Dist']   = df['Odd_Even'].apply(lambda x: odd_even_dist(str(x)))
    
    #Convert to numeric
    logger.debug("Converting results to numbers")
    df[['col1','col2','col3','col4','col5','col6']] = df[['col1','col2','col3','col4','col5','col6']].apply(pd.to_numeric)
    
    #Rename
    logger.debug("Renaming columns")
    for i in range(0, len(col_list)):
        val = 'col' + str(i+1)
        df = df.rename(columns={val:col_list[i]})
    df = df.rename(columns={'col0':'Date'})
    
    df = df[['Date', 'Winning Numbers', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'Day_Name', 'Odd_Even', 'Odd_Even_Dist']]
    
    try:
        df.to_excel(filename_1995)
    except Exception as e:
        logger.error("Exception: " + str(e))
    else:
        logger.debug("Exported to excel")

if __name__ == "__main__":
    main()