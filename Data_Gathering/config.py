from datetime import date
from datetime import datetime

today = date.today()
d1    = today.strftime("%m-%d-%Y")
t1    = str(datetime.now().hour) + "-" + str(datetime.now().minute) + "-" + str(datetime.now().second)

filename_log   = 'C:\Personal_Project\Lotto_Analysis\Logs\{}_{}_scrape.txt'.format(d1,t1)
filename_excel = 'C:\Personal_Project\Lotto_Analysis\Data_Gathering\PastDataResults.xlsx'

url_list = []

for i in range(1,15):
    page   = str(i)
    clause = "&orderby=new"
    url    = "https://www.lotto-8.com/philippines/listltoPH42.asp?indexpage={}{}".format(page,clause)
    url_list.append(url)