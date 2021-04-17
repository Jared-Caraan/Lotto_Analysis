import pandas as pd
import logging

from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from config import delta_log, filename_default, default_batch

# Logger Configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler(delta_log)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def main():
    
    # Past data
    try:
        df_past = pd.read_excel(filename_default)
    except Exception as e:
        logger.error("Exception: " + str(e))
    else:
        logger.debug("Opening past data")
    print('a')
    
    # Ignore USB error; browser to not popup
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #options.add_argument("--headless")
    
    # Access Chrome website
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)
        driver.get(default_batch)
    except Exception as e:
        logger.critical("Exception: " + str(e))
    else:
        logger.debug("Accessing website")
    print('b')
    
    # Interact with drop-down menu
    filter_game = driver.find_element_by_xpath('//select[@id="LotteryName"]')
    
    # Choose the option with value "6/42 Lotto" from the drop-down
    for option in filter_game.find_elements_by_tag_name('option'):
        if option.text == '6/42 Lotto':
            option.click()
            break
    
    # Click submit button
    driver.find_element_by_xpath('//input[@value="Search Numbers"]').click()
    
    # Load first batch
    date_record = driver.find_elements_by_xpath('//table/tbody/tr/td[@title="Draw date"]')
    draw_record = driver.find_elements_by_xpath('//table/tbody/tr/td[3]/span')
    print('c')
    
    #driver.implicitly_wait(30)
    
    logger.debug("Latest date: " + date_record[0].text)
    date_val = datetime.strptime(date_record[0].text, '%d %b, %Y')
    print('d')
    
    if date_val == df_past['Date'].iloc[0]:
        logger.debug("No new records")
    else:
        df_new = pd.DataFrame(list(zip([date_val], [draw_record[0].get_attribute('title')])), columns = ['Date', 'Draw'])
        df_new[['first', 'second', 'third', 'fourth', 'fifth', 'sixth']] = df_new['Draw'].str.split('-', expand = True)
        
        try:
            df_new = df_new.append(df_past, sort = False, ignore_index = True)
            df_new.to_excel(filename_default, index = False)
        except Exception as e:
            logger.error("Exception: " + str(e))
        else:
            logger.debug("Adding newest date: " + str(df_new["Date"].iloc[0]))
            logger.debug("Newest winning number: " + str(df_new["Draw"].iloc[0]))
    

if __name__ == "__main__":
    main()