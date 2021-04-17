import pandas as pd

from selenium import webdriver
from config import chromedriver, second_batch, filename_2005

def date_name(x):
    
    return x[:x.index(',')]

def separate(x):
    
    return x[x.index(',')+2:]
    
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
    
    return df['first'] + ',' + df['second'] + ',' + df['third'] + ',' + df['fourth'] + ',' + df['fifth'] + ',' +  df['sixth']

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
    
    # Go back to third to the last page
    driver.find_element_by_xpath('//table[@class="FDPagerLeft"]/tbody/tr/td[7]/img[@class="ccpoint"]').click()
    driver.find_element_by_xpath('//table[@class="FDPagerLeft"]/tbody/tr/td[2]/img[@class="ccpoint"]').click()
    driver.find_element_by_xpath('//table[@class="FDPagerLeft"]/tbody/tr/td[2]/img[@class="ccpoint"]').click()
    
    # Load third to the last page
    date_table   = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[@class="restcdd"]')
    first_table  = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[3]')
    second_table = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[4]')
    third_table  = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[5]')
    fourth_table = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[6]')
    fifth_table  = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[7]')
    sixth_table  = driver.find_elements_by_xpath('//table[@class="restbl"]/tbody/tr/td[8]')
    
    for p in range(len(date_table)):
        row_date.append(date_table[p].text)
        row_second.append(second_table[p].text)
        row_third.append(third_table[p].text)
        row_fourth.append(fourth_table[p].text)
        row_fifth.append(fifth_table[p].text)
        row_sixth.append(sixth_table[p].text)
    
    for p in range(1, len(first_table)):
        row_first.append(first_table[p].text)
        
    driver.implicitly_wait(10)
    
    # Load second to the last page
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
        row_second.append(second_table[p].text)
        row_third.append(third_table[p].text)
        row_fourth.append(fourth_table[p].text)
        row_fifth.append(fifth_table[p].text)
        row_sixth.append(sixth_table[p].text)
    
    for p in range(1, len(first_table)):
        row_first.append(first_table[p].text)
        
    driver.implicitly_wait(10)
    
    # Load last page
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
        row_second.append(second_table[p].text)
        row_third.append(third_table[p].text)
        row_fourth.append(fourth_table[p].text)
        row_fifth.append(fifth_table[p].text)
        row_sixth.append(sixth_table[p].text)
    
    for p in range(1, len(first_table)):
        row_first.append(first_table[p].text)
        
    driver.close()
    
    # Create dataframe
    df = pd.DataFrame(list(zip(row_date, row_first, row_second, row_third, row_fourth, row_fifth, row_sixth)), 
                        columns = ['Date', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth'])
    
    df['Day_Name'] = df['Date'].apply(lambda x: date_name(x))
    df['Date']     = df['Date'].apply(lambda x: separate(x))
    df['Date']     = pd.to_datetime(df['Date'], format = '%B %d, %Y')
    
    df['Winning Numbers'] = df.apply(join, axis = 1)
    df['Odd_Even']        = df['Winning Numbers'].apply(lambda x: odd_even(x))
    df['Odd_Even_Dist']   = df['Odd_Even'].apply(lambda x: odd_even_dist(str(x)))
    
    #Convert to numeric
    df['first']  = df['first'].astype(int)
    df['second'] = df['second'].astype(int)
    df['third']  = df['third'].astype(int)
    df['fourth'] = df['fourth'].astype(int)
    df['fifth']  = df['fifth'].astype(int)
    df['sixth']  = df['sixth'].astype(int)
    
    df = df[['Date', 'Winning Numbers', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'Day_Name', 'Odd_Even', 'Odd_Even_Dist']]
    
    # Export to excel
    df.to_excel(filename_2005, index = False)
 
if __name__ == "__main__":
    main()