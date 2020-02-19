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
    
def transform(soup):

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
    
    return final_list
    
def main():
    
    #Create new dataframe
    df = pd.DataFrame()

    #Get response from website 
    for i in range(1,6):
        page = str(i)
        clause = "&orderby=new"
        url = "https://www.lotto-8.com/philippines/listltoPH42.asp?indexpage={}{}".format(page,clause)
        response = requests.get(url)
        print("Page: " + page + ": " + str(response))
    
        #Parsing the html structure
        soup = BeautifulSoup(response.text, "html.parser")
        
        page_row = transform(soup)
        print("Page: " + page + ": " + "Extracting dates and numbers")
        
        df = df.append(page_row, ignore_index = True)
        print("Page: " + page + ": " + "Appending to DataFrame")
    
    df = df.rename(columns={0: "Date", 1: "Winning Numbers"})
    print(df)

if __name__ == "__main__":
    main()