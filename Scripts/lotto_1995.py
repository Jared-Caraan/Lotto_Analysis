import requests
import logging

from bs4 import BeautifulSoup
from config import scrape_log, first_batch

##Logger Configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler(scrape_log)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def extract_date(a):
    
    a = str(a).replace("<td>", "")
    a = str(a).replace ("</td>", "")
    a = str(a).strip()
    
    return a

def main():
    
    try:
        response = requests.get(first_batch)
    except Exception as e:
        print(str(e))
    else:
        print("nice")
        
    #Parsing the html structure
    soup = BeautifulSoup(response.text, "html.parser")
    
    row = soup.findAll('td')
    row_dates = row[0::7]
    row_dates = map(extract_date,row_dates)
    print(list(row_dates))

if __name__ == "__main__":
    main()