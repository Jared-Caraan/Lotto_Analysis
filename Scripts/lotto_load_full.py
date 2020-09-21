import requests
import urllib.request
import logging
import pandas as pd

from bs4 import BeautifulSoup
from config import scrape_log, filename_excel, url_list

##Logger Configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler(scrape_log)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

##Removing HTML Tags to snip only the date
def extract_date(a):

    a   = str(a).replace("<br>", "<br/>")
    br  = "<br/>"
    ind = str(a).index(br)
    res = a[(len(br)+ind):(len(br)+ind)+10]
    
    return res

##Removing HTML Tags to snip only the winning numbers
def extract_num(a):

    a   = str(a).replace(u'\xa0', '')
    br  = "<br/>"
    ind = str(a).index(br)
    res = a[(len(br)+ind):(len(br)+ind)+17]
    
    return res

##Data Transformation to return only the date and the winning numbers
def transform(soup):

    row       = soup.findAll('td')
    row_slice = row[2:len(row)-1]
    row_dates = row_slice[0::2]
    row_num   = row_slice[1::2]
    
    row_extract_date = map(extract_date, row_dates)
    row_extract_num  = map(extract_num, row_num)
    
    final_list = list(zip(row_extract_date,row_extract_num))
    
    return final_list

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
    
def main():
    
    ##Create new dataframe
    df = pd.DataFrame()

    ##Get response from website 
    for idx, val in enumerate(url_list):
        try:
            response = requests.get(val)
        except:
            logger.error(str(response))
        else:
            logger.debug("Page: " + str(idx+1) + ": " + str(response))
    
        ##Parsing the html structure
        soup = BeautifulSoup(response.text, "html.parser")
        
        page_row = transform(soup)
        logger.debug("Page: " + str(idx+1) + ": " + "Extracting dates and numbers")
        
        df = df.append(page_row, ignore_index = True)
        logger.debug("Page: " + str(idx+1) + ": " + "Appending to DataFrame")
    
    ##Rename columns
    df = df.rename(columns={0: "Date", 1: "Winning Numbers"})
    logger.debug("Renaming columns")
    
    ##Splitting values into different columns
    df[['first', 'second', 'third', 'fourth', 'fifth', 'sixth']] = df['Winning Numbers'].str.split(',', expand=True)
    logger.debug("Splitting numbers into columns")
    
    ##Adding date detail
    df['Date'] = pd.to_datetime(df['Date'], format = '%d/%m/%Y')
    df['Day_Name'] = df['Date'].dt.day_name()
    
    ##Odd-Column Pattern
    df['Odd_Even'] = df['Winning Numbers'].apply(lambda x: odd_even(str(x)))
    
    df['Odd_Even_Dist'] = df['Odd_Even'].apply(lambda x: odd_even_dist(str(x)))
    
    logger.debug(df.head(5))
    logger.debug(df.tail(5))
    
    ##Remove duplicates
    logger.debug("Removing duplicates (if there's any)")
    df.drop_duplicates(inplace=True, ignore_index=True)
    
    ##Transferring to Excel
    try:
        df.to_excel(filename_excel)
    except Exception as e:
        logger.error("Exception: " + str(e))
    else:
        logger.debug("Excel file generated successfully")

if __name__ == "__main__":
    main()