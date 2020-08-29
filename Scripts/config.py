from datetime import date
from datetime import datetime
from pandas.api.types import CategoricalDtype

## DATE CONFIGURATIONS
today = date.today()
d1    = today.strftime("%m-%d-%Y")
t1    = str(datetime.now().hour) + "-" + str(datetime.now().minute) + "-" + str(datetime.now().second)

weekday  = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_type = CategoricalDtype(categories=weekday, ordered=True)

## FILES
filename_excel    = 'C:\Personal_Project\Lotto_Analysis\Data_Gathering\PastDataResults.xlsx'
filename_rng_test = 'C:\Personal_Project\Lotto_Analysis\Data_Gathering\RNG_test.xlsx'
filename_z_score  = 'C:\Personal_Project\Lotto_Analysis\Data_Gathering\z_score.xlsx'
filename_odd_even = 'C:\Personal_Project\Lotto_Analysis\Data_Gathering\odd_even.xlsx'
filename_archive  = r'C:\Personal_Project\Lotto_Analysis\Archive\{}_log.zip'.format(d1)

## DIRECTORY
scrape_archive     = r'C:\Personal_Project\Lotto_Analysis\Logs\Scrape'
delta_archive      = r'C:\Personal_Project\Lotto_Analysis\Logs\Delta'
visual_archive     = r'C:\Personal_Project\Lotto_Analysis\Logs\Visual'
train_archive      = r'C:\Personal_Project\Lotto_Analysis\Logs\Train'
score_archive      = r'C:\Personal_Project\Lotto_Analysis\Logs\Score'

## LOG
scrape_log  = 'C:\Personal_Project\Lotto_Analysis\Logs\Scrape\{}_{}_scrape.txt'.format(d1,t1)
delta_log   = 'C:\Personal_Project\Lotto_Analysis\Logs\Delta\{}_{}_delta.txt'.format(d1,t1)
visual_log  = 'C:\Personal_Project\Lotto_Analysis\Logs\Visual\{}_{}_visual.txt'.format(d1,t1)
train_log   = 'C:\Personal_Project\Lotto_Analysis\Logs\Train\{}_{}_train.txt'.format(d1,t1)
score_log   = 'C:\Personal_Project\Lotto_Analysis\Logs\Score\{}_{}_score.txt'.format(d1,t1)

## MODEL
pickle_odd_even   = r'C:\Personal_Project\Lotto_Analysis\Model\odd_even_model.pkl'
pickle_first      = r'C:\Personal_Project\Lotto_Analysis\Model\first_model.pkl'

## SCALER
scaler_odd_even   = r'C:\Personal_Project\Lotto_Analysis\Model\odd_even_scaler.pkl'
scaler_first      = r'C:\Personal_Project\Lotto_Analysis\Model\first_scaler.pkl'

## URL SCRAPING
url_list = []

for i in range(1,64):
    page   = str(i)
    clause = "&orderby=new"
    url    = "https://www.lotto-8.com/philippines/listltoPH42.asp?indexpage={}{}".format(page,clause)
    url_list.append(url)
    
## Hyperparameters
num_prediction = 1
look_back      = 2
epoch          = 400
test_size      = 0.2
rand_state     = 10
n_estimators   = 10
criterion      = 'entropy'
