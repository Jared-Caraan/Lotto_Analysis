import pandas as pd
import statistics

from config import filename_all

def getMean(row):
    return round((row['first'] + row['second'] + row['third'] + row['fourth'] + row['fifth'] + row['sixth']) / 6, 2)

def getStdev(row):
    return round(statistics.pstdev([row['first'],row['second'],row['third'],row['fourth'],row['fifth'],row['sixth']]),2)

df_past = pd.read_excel(filename_all)
df_past['Average'] = df_past.apply(getMean, axis=1)
df_past['St. Dev'] = df_past.apply(getStdev, axis=1)
# print(len(df_past))
df_past.to_excel(filename_all, index = False)

# print(df_past.head())