import pandas as pd

from WebTable import WebTable
from selenium import webdriver
from config import chromedriver, second_batch

def main():
    
    row_date   = []
    row_first  = []
    row_second = []
    row_third  = []
    row_fourth = []
    row_fifth  = []
    row_sixth  = []
    
    #Access Chrome website
    driver = webdriver.Chrome(executable_path = chromedriver)
    driver.get(second_batch)
    
    #Interact with drop-down menu
    num_pages = driver.find_element_by_xpath('//select[@class="FDPerPageDDL"]')
    
    #Choose the option with value "100" from the drop-down
    for option in num_pages.find_elements_by_tag_name('option'):
        if option.text == '100':
            option.click()
            break
    
    #Implicitly wait for the page to load
    driver.implicitly_wait(30)
    
    # button
    driver.find_element_by_xpath('//table[@class="FDPagerLeft"]/tbody/tr/td[7]/img[@class="ccpoint"]').click()
    driver.find_element_by_xpath('//table[@class="FDPagerLeft"]/tbody/tr/td[2]/img[@class="ccpoint"]').click()
    driver.find_element_by_xpath('//table[@class="FDPagerLeft"]/tbody/tr/td[2]/img[@class="ccpoint"]').click()
    
    date_table   = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[@class="restcdd"]')
    first_table  = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[3]')
    second_table = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[4]')
    third_table  = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[5]')
    fourth_table = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[6]')
    fifth_table  = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[7]')
    sixth_table  = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[8]')
    
    for p in range(len(date_table)):
        row_date.append(date_table[p].text)
    
    for p in range(1, len(first_table)-1):
        row_first.append(first_table[p].text)
        row_second.append(second_table[p].text)
        row_third.append(third_table[p].text)
        row_fourth.append(fourth_table[p].text)
        row_fifth.append(fifth_table[p].text)
        row_sixth.append(sixth_table[p].text)
    
    driver.find_element_by_xpath('//table[@class="FDPagerLeft"]/tbody/tr/td[8]/img[@class="ccpoint"]').click()
    date_table = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[@class="restcdd"]')
    first_table  = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[3]')
    second_table = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[4]')
    third_table  = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[5]')
    fourth_table = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[6]')
    fifth_table  = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[7]')
    sixth_table  = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[8]')
    
    for p in range(len(date_table)):
        row_date.append(date_table[p].text)
    
    for p in range(1, len(first_table)-1):
        row_first.append(first_table[p].text)
        row_second.append(second_table[p].text)
        row_third.append(third_table[p].text)
        row_fourth.append(fourth_table[p].text)
        row_fifth.append(fifth_table[p].text)
        row_sixth.append(sixth_table[p].text)
        
    driver.find_element_by_xpath('//table[@class="FDPagerLeft"]/tbody/tr/td[8]/img[@class="ccpoint"]').click()
    date_table = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[@class="restcdd"]')
    first_table  = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[3]')
    second_table = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[4]')
    third_table  = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[5]')
    fourth_table = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[6]')
    fifth_table  = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[7]')
    sixth_table  = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[8]')
    
    for p in range(len(date_table)):
        row_date.append(date_table[p].text)
    
    for p in range(1, len(first_table)-1):
        row_first.append(first_table[p].text)
        row_second.append(second_table[p].text)
        row_third.append(third_table[p].text)
        row_fourth.append(fourth_table[p].text)
        row_fifth.append(fifth_table[p].text)
        row_sixth.append(sixth_table[p].text)
    
    df = pd.DataFrame(list(zip(row_date, row_first, row_second, row_third, row_fourth, row_fifth, row_sixth)), 
                        columns = ['Date', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth'])
    
    print(df.head())
    print(df.tail())
 
    driver.close()

if __name__ == "__main__":
    main()