from datetime import date
from datetime import datetime
from pandas.api.types import CategoricalDtype

## DATE CONFIGURATIONS
today = date.today()
d1    = today.strftime("%m-%d-%Y")
t1    = str(datetime.now().hour) + "-" + str(datetime.now().minute) + "-" + str(datetime.now().second)

col_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
weekday  = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_type = CategoricalDtype(categories=weekday, ordered=True)

## FILES
filename_excel    = 'C:\Personal_Project\Lotto_Analysis\Data_Gathering\PastDataResults.xlsx'
filename_1995     = 'C:\Personal_Project\Lotto_Analysis\Data_Gathering\Results_1995.xlsx'
filename_2005     = 'C:\Personal_Project\Lotto_Analysis\Data_Gathering\Results_2005.xlsx'
filename_all      = 'C:\Personal_Project\Lotto_Analysis\Data_Gathering\Results_all.xlsx'
filename_rng_test = 'C:\Personal_Project\Lotto_Analysis\Data_Gathering\RNG_test.xlsx'
filename_z_score  = 'C:\Personal_Project\Lotto_Analysis\Data_Gathering\z_score.xlsx'
filename_odd_even = 'C:\Personal_Project\Lotto_Analysis\Data_Gathering\odd_even.xlsx'
filename_archS    = r'C:\Personal_Project\Lotto_Analysis\Archive\{}_scrape.zip'.format(d1)
filename_archD    = r'C:\Personal_Project\Lotto_Analysis\Archive\{}_delta.zip'.format(d1)
filename_archV    = r'C:\Personal_Project\Lotto_Analysis\Archive\{}_visual.zip'.format(d1)
filename_archT    = r'C:\Personal_Project\Lotto_Analysis\Archive\{}_train.zip'.format(d1)
filename_archP    = r'C:\Personal_Project\Lotto_Analysis\Archive\{}_predict.zip'.format(d1)

## DIRECTORY
scrape_archive = r'C:\Personal_Project\Lotto_Analysis\Logs\Scrape'
delta_archive  = r'C:\Personal_Project\Lotto_Analysis\Logs\Delta'
visual_archive = r'C:\Personal_Project\Lotto_Analysis\Logs\Visual'
train_archive  = r'C:\Personal_Project\Lotto_Analysis\Logs\Train'
score_archive  = r'C:\Personal_Project\Lotto_Analysis\Logs\Score'
delete_zipped  = r'C:\Personal_Project\Lotto_Analysis\Archive'

## LOG
scrape_log = 'C:\Personal_Project\Lotto_Analysis\Logs\Scrape\{}_{}_scrape.txt'.format(d1,t1)
delta_log  = 'C:\Personal_Project\Lotto_Analysis\Logs\Delta\{}_{}_delta.txt'.format(d1,t1)
visual_log = 'C:\Personal_Project\Lotto_Analysis\Logs\Visual\{}_{}_visual.txt'.format(d1,t1)
train_log  = 'C:\Personal_Project\Lotto_Analysis\Logs\Train\{}_{}_train.txt'.format(d1,t1)
score_log  = 'C:\Personal_Project\Lotto_Analysis\Logs\Score\{}_{}_score.txt'.format(d1,t1)

## MODEL
pickle_odd_even = r'C:\Personal_Project\Lotto_Analysis\Model\odd_even_model.pkl'
model_num       = r'C:\Personal_Project\Lotto_Analysis\Model\model'

## SCALER
scaler_odd_even = r'C:\Personal_Project\Lotto_Analysis\Model\odd_even_scaler.pkl'
scaler_num      = r'C:\Personal_Project\Lotto_Analysis\Model\scaler'

## URL SCRAPING
url_list = []

for i in range(1,64):
    page   = str(i)
    clause = "&orderby=new"
    url    = "https://www.lotto-8.com/philippines/listltoPH42.asp?indexpage={}{}".format(page,clause)
    url_list.append(url)

first_batch = "https://lottotips888.blogspot.com/2008/09/philippine-lotto-results-642-year-1995.html"
second_batch = "http://www.theluckygene.com/LotteryResults.aspx?gid=LottoPH"
    
## Hyperparameters
test_size      = 0.15
rand_state     = 10
n_estimators   = 10
criterion      = 'entropy'

## DRIVER
chromedriver = 'C:\Driver\chromedriver_win32\chromedriver.exe'
