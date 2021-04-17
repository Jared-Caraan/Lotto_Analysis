import pandas as pd
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from config import chromedriver, default_batch

def main():
    
    #Ignore USB error
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    #Access Chrome website
    driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)
    driver.get(default_batch)
    
    
    #Interact with drop-down menu
    filter_game = driver.find_element_by_xpath('//select[@id="LotteryName"]')
    print('a')
    
    #Choose the option with value "6/42 Lotto" from the drop-down
    for option in filter_game.find_elements_by_tag_name('option'):
        if option.text == '6/42 Lotto':
            option.click()
            break
    print('b')
    
    # Click submit button
    driver.find_element_by_xpath('//input[@value="Search Numbers"]').click()
    print('c')
    
    time.sleep(60)
    driver.close()

if __name__ == "__main__":
    main()