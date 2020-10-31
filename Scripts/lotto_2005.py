from WebTable import WebTable
from selenium import webdriver
from config import chromedriver, second_batch

def main():
    
    #Access Chrome website
    driver = webdriver.Chrome(executable_path = chromedriver)
    driver.get(second_batch)
    
    #Interact with drop-down menu
    num_pages = driver.find_element_by_xpath('//select[@class="FDPerPageDDL"]')
    table = WebTable(driver.find_element_by_xpath('//*[@id="FDResultsContainer"]/div[2]/table'))
    
    print(str(table.get_row_count()))
    
    #Choose the option with value "100" from the drop-down
    for option in num_pages.find_elements_by_tag_name('option'):
        if option.text == '100':
            option.click()
            break
    
    #Implicitly wait for the page to load
    driver.implicitly_wait(30)
    
    #Scrape the data from the table with 100 rows
    # rows_date = driver.find_elements_by_xpath('//td[@class="restcdd"]')
    # rows_num  = driver.find_elements_by_xpath('//td[@class="restc"]')
    
    # date_list = []
    # num_list = []
    
    # for p in range(len(rows_date)):
        # date_list.append(rows_date[p].text)
        # num_list.append(rows_num[p].text)
    
    
        
    driver.close()
    
    #print(num_list)

if __name__ == "__main__":
    main()