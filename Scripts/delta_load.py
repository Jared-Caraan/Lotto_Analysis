import requests
import urllib.request
import pandas as pd
import logging

from bs4 import BeautifulSoup
from config import delta_log, filename_excel, url_list

#Logger Configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler(delta_log)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

#Removing HTML Tags to snip only the date
def extract_date(a):

    a   = str(a).replace("<br>", "<br/>")
    br  = "<br/>"
    ind = str(a).index(br)
    res = a[(len(br)+ind):(len(br)+ind)+10]
    
    return res

#Removing HTML Tags to snip only the winning numbers
def extract_num(a):

    a   = str(a).replace(u'\xa0', '')
    br  = "<br/>"
    ind = str(a).index(br)
    res = a[(len(br)+ind):(len(br)+ind)+17]
    
    return res

#Data Transformation to return only the date and the winning numbers
def transform(soup):

    row       = soup.findAll('td')
    row_dates = row[2]
    row_num   = row[3]
    
    row_extract_date = extract_date(row_dates)
    row_extract_num  = extract_num(row_num)
    
    final_list = [row_extract_date, row_extract_num]
    
    return final_list

def main():

    #Create new dataframe
    df = pd.DataFrame(columns = ["Date", "Winning Numbers"])
    
    val = url_list[0]

    try:
        response = requests.get(val)
    except Exception as e:
        logger.critical("Exception: " + str(e))
    else:
        logger.debug(str(response))
        
    #Parsing the html structure
    soup = BeautifulSoup(response.text, "html.parser")
    
    page_row = transform(soup)
    logger.debug("Extracting dates and numbers")
    
    df = df.append({'Date': page_row[0], 'Winning Numbers': page_row[1]}, ignore_index = True)
    df[['first', 'second', 'third', 'fourth', 'fifth', 'sixth']] = df['Winning Numbers'].str.split(',', expand=True)
    logger.debug("Appending to DataFrame")
        
    #Fetching the latest past result from the xlsx
    try:
        df_past = pd.read_excel(filename_excel)
    except Exception as e:
        logger.error("Exception: " + str(e))
    else:
        logger.debug("Reading historical data")
        
    logger.debug("Latest date would be: " + str(df_past["Date"].head(1)))
    
    #Comparison of the past results and the daily checking
    if str(df["Date"].head(1)) == str(df_past["Date"].head(1)):
        logger.debug("No new records")
    else:
        try:
            df = df.append(df_past, sort = False, ignore_index = True)
            df.drop(columns = ['Unnamed: 0'], inplace = True)
            df.to_excel(filename_excel)
        except Exception as e:
            logger.error("Exception: " + str(e))
        else:
            logger.debug("Adding newest date: " + str(df["Date"].head(1)))
            logger.debug("Newest winning number: " + str(df["Winning Numbers"].head(1)))
    
if __name__ == "__main__":
    main()