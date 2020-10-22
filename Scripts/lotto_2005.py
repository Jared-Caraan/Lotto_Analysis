from selenium import webdriver

from config import chromedriver, second_batch

def main():
    
    driver = webdriver.Chrome(executable_path = chromedriver)
    driver.get(second_batch)
    
    num_pages = driver.find_element_by_xpath('//select[@class="FDPerPageDDL"]')
    
    for option in num_pages.find_elements_by_tag_name('option'):
        if option.text == '100':
            option.click()
            break
    
    driver.implicitly_wait(30)
    
    rows = driver.find_elements_by_xpath('//td[@class="restcdd"]')
    date_list = []
    
    for p in range(len(rows)):
        date_list.append(rows[p].text)
    
    driver.close()
    
    print(date_list)

if __name__ == "__main__":
    main()