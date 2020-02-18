import requests
import urllib.request
import time
import pandas as pd
from bs4 import BeautifulSoup

def extract_date(a):

    a = str(a).replace("<br>", "<br/>")
    br = "<br/>"
    ind = str(a).index(br)
    res = a[(len(br)+ind):(len(br)+ind)+10]
    
    return res
    
def extract_num(a):

    a = str(a).replace(u'\xa0', '')
    br = "<br/>"
    ind = str(a).index(br)
    res = a[(len(br)+ind):(len(br)+ind)+17]
    
    return res

def main():
    #Get response from website
    try:
        url = "https://www.lotto-8.com/philippines/listltoPH42.asp?indexpage=1"
        response = requests.get(url)
        print(response)
    except:
        print("Error")
    
    #Parsing the html structure
    soup = BeautifulSoup(response.text, "html.parser")
    
    #Getting the right elements (dates and winning numbers)
    row = soup.findAll('td')
    row_slice = row[2:len(row)-1]
    row_dates = row_slice[0::2]
    row_num = row_slice[1::2]
    
    #Getting only the dates
    row_extract_date = map(extract_date, row_dates)
    
    #Getting the winning numbers
    row_extract_num = map(extract_num, row_num)
    
    #consolidate lists
    final_list = list(zip(row_extract_date,row_extract_num))
    
    #Create new dataframe
    df = pd.DataFrame(final_list, columns = ['Date', 'Numbers'])
    
    print(df)

if __name__ == "__main__":
    main()