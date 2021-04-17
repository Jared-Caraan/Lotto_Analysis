import pandas as pd
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from config import chromedriver, default_batch, filename_default

def main():
    
    date_holder = []
    draw_holder = []
    
    # Ignore USB error
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    # Access Chrome website
    driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)
    driver.get(default_batch)
    
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
    
    # Append to holders
    for i in range(len(date_record)):
        date_holder.append(date_record[i].text)
    
    for j in range(len(draw_record)):
        draw_holder.append(draw_record[j].get_attribute('title'))
    
    for k in range(8, 0, -1):
        filter_date = driver.find_element_by_xpath('//select[@id="LotteryDate"]')
        for option in filter_date.find_elements_by_tag_name('option'):
            opt = '2017-0{}'.format(str(k))
            if option.text == opt:
                option.click()
                break
        driver.find_element_by_xpath('//input[@value="Search Numbers"]').click()
        date_record = driver.find_elements_by_xpath('//table/tbody/tr/td[@title="Draw date"]')
        draw_record = driver.find_elements_by_xpath('//table/tbody/tr/td[3]/span')
        for l in range(len(date_record)):
            date_holder.append(date_record[l].text)
        for m in range(len(draw_record)):
            draw_holder.append(draw_record[m].get_attribute('title'))
    
    # DataFrame
    df = pd.DataFrame(list(zip(date_holder, draw_holder)), columns = ['Date', 'Draw'])
    df.drop_duplicates(inplace = True)
    
    # Features
    df['Date'] = pd.to_datetime(df['Date'], format = '%d %b, %Y')
    df[['first', 'second', 'third', 'fourth', 'fifth', 'sixth']] = df['Draw'].str.split('-', expand = True)
    
    print(df.head(5))
    
    # Export
    df.to_excel(filename_default, index = False)
    
    time.sleep(20)
    driver.close()

if __name__ == "__main__":
    main()