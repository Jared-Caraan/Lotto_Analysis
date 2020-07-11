from datetime import date
from datetime import datetime
from pandas.api.types import CategoricalDtype

## DATE CONFIGURATIONS
today = date.today()
d1    = today.strftime("%m-%d-%Y")
t1    = str(datetime.now().hour) + "-" + str(datetime.now().minute) + "-" + str(datetime.now().second)

weekday = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_type = CategoricalDtype(categories=weekday, ordered=True)

## FILES
filename_log      = 'C:\Personal_Project\Lotto_Analysis\Logs\{}_{}_scrape.txt'.format(d1,t1)
filename_excel    = 'C:\Personal_Project\Lotto_Analysis\Data_Gathering\PastDataResults.xlsx'
filename_rng_test = 'C:\Personal_Project\Lotto_Analysis\Data_Gathering\RNG_Tests.xlsx'
filename_archive  = r'C:\Personal_Project\Lotto_Analysis\Archive\{}_log.zip'.format(d1)

## DIRECTORY
dir_archive      = r'C:\Personal_Project\Lotto_Analysis\Logs'

## LOG
delta_log   = 'C:\Personal_Project\Lotto_Analysis\Logs\{}_{}_delta.txt'.format(d1,t1)
visual_log  = 'C:\Personal_Project\Lotto_Analysis\Logs\{}_{}_visual.txt'.format(d1,t1)
predict_log = 'C:\Personal_Project\Lotto_Analysis\Logs\{}_{}_visual.txt'.format(d1,t1)

## URL SCRAPING
url_list = []

for i in range(1,15):
    page   = str(i)
    clause = "&orderby=new"
    url    = "https://www.lotto-8.com/philippines/listltoPH42.asp?indexpage={}{}".format(page,clause)
    url_list.append(url)
    
## RNN
num_prediction = 1
look_back      = 2
epoch          = 400
