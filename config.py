from datetime import date
from datetime import datetime
from pandas.api.types import CategoricalDtype
from scipy.stats import randint

# DATE CONFIGURATIONS
today = date.today()
d1    = today.strftime("%Y-%m-%d")
t1    = str(datetime.now().hour) + "-" + str(datetime.now().minute) + "-" + str(datetime.now().second)

col_list   = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
weekday    = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
day_type   = CategoricalDtype(categories=weekday, ordered=True)
month_type = CategoricalDtype(categories=month_list, ordered=True)

# PLOTLY CONFIGURATIONS
username = 'rubberninja'
api_key = 'FUPGqd08gWsRPq0PJP65'

# FILES
filename_excel    = r'C:\Users\Jared\Documents\Lotto_Analysis\Data_Gathering\PastDataResults.xlsx'
filename_1995     = r'C:\Users\Jared\Documents\Lotto_Analysis\Data_Gathering\Results_1995.xlsx'
filename_2005     = r'C:\Users\Jared\Documents\Lotto_Analysis\Data_Gathering\Results_2005.xlsx'
filename_all      = r'.\Lotto_Analysis\Data_Gathering\Results_all.xlsx'
filename_default  = r'C:\Users\Jared\Documents\Lotto_Analysis\Data_Gathering\Results_default.xlsx'
filename_refact   = r'C:\Users\Jared\Documents\Lotto_Analysis\Data_Gathering\Results_refactored.csv'
filename_csv_date = r'C:\Users\Jared\Documents\Lotto_Analysis\Data_Gathering\Results_refact_date.csv'
filename_rng_test = r'C:\Users\Jared\Documents\Lotto_Analysis\Data_Gathering\RNG_test.xlsx'
filename_z_score  = r'C:\Users\Jared\Documents\Lotto_Analysis\Data_Gathering\z_score.xlsx'
filename_odd_even = r'C:\Users\Jared\Documents\Lotto_Analysis\Data_Gathering\odd_even.xlsx'
filename_archive  = r'C:\Users\Jared\Documents\Lotto_Analysis\Archive\{}_.zip'.format(d1)

# DIRECTORY
delete_zipped  = r'C:\Users\Jared\Documents\Lotto_Analysis\Archive'
archive_files  = r'C:\Users\Jared\Documents\Lotto_Analysis\Logs'

# LOG
scrape_log = r'C:\Users\Jared\Documents\Lotto_Analysis\Logs\Scrape\{}_{}_scrape.txt'.format(d1,t1)
delta_log  = r'C:\Users\Jared\Documents\Lotto_Analysis\Logs\Delta\{}_{}_delta.txt'.format(d1,t1)
visual_log = r'C:\Users\Jared\Documents\Lotto_Analysis\Logs\Visual\{}_{}_visual.txt'.format(d1,t1)
train_log  = r'C:\Users\Jared\Documents\Lotto_Analysis\Logs\Train\{}_{}_train.txt'.format(d1,t1)
score_log  = r'C:\Users\Jared\Documents\Lotto_Analysis\Logs\Score\{}_{}_score.txt'.format(d1,t1)

# MODEL
pickle_odd_even = r'C:\Users\Jared\Documents\Lotto_Analysis\Model\odd_even_model.pkl'
model_num       = r'C:\Users\Jared\Documents\Lotto_Analysis\Model\model'

# SCALER
scaler_odd_even = r'C:\Users\Jared\Documents\Lotto_Analysis\Model\odd_even_scaler.pkl'
scaler_num      = r'C:\Users\Jared\Documents\Lotto_Analysis\Model\scaler'

# LABEL ENCODER
le_day = r'C:\Users\Jared\Documents\Lotto_Analysis\Model\le_day'
le_y   = r'C:\Users\Jared\Documents\Lotto_Analysis\Model\le_y'

# ONE HOT ENCODER
ohe_num = r'C:\Users\Jared\Documents\Lotto_Analysis\Model\ohe'

# URL SCRAPING
url_list = []

for i in range(1,70):
    page   = str(i)
    clause = "&orderby=new"
    url    = "https://www.lotto-8.com/philippines/listltoPH42.asp?indexpage={}{}".format(page,clause)
    url_list.append(url)

first_batch = "https://lottotips888.blogspot.com/2008/09/philippine-lotto-results-642-year-1995.html"
second_batch = "http://www.theluckygene.com/LotteryResults.aspx?gid=LottoPH"
default_batch = "https://www.businesslist.ph/lottery/results/history"
    
# HYPERPARAMETERS (DECISION TREE)
test_size      = 0.15
rand_state     = 10
n_estimators   = 10
criterion      = 'entropy'

model_params = {
    'n_estimators': randint(3,100),
    'criterion': ['entropy', 'gini']
}

# HYPERPARAMETERS (NEURAL NETWORK)
lr_nn = 0.001
rho_nn = 0.95
eps_nn = 1e-07
epoch_nn = 5000
batch_nn = 10

# DRIVER
chromedriver = r'C:\Users\Jared\Documents\Driver\chromedriver.exe'