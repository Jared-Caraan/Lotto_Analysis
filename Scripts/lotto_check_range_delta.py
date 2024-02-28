import pandas as pd
import logging

from config import filename_all, filename_range, range_log

#Logger Configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler(range_log)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def checkRange(df):

    df['Month_num'] = df['Date'].dt.strftime('%m').str.lstrip("0")
    df['Day'] = df['Date'].dt.strftime('%d')
    df['Day'] = df['Day'].str.lstrip("0")
    
    rows = []

    criteria_list = ['day_name', 'month_day']

    for i in criteria_list:
        holder_dict = {}
        holder_dict['Date'] = df['Date'].iloc[0]
        holder_dict['Winning Numbers'] = df['Winning Numbers'].iloc[0]

        if i == 'day_name':
            filter = df['Day_Name'] == df['Day_Name'].iloc[0]
            holder_dict['Criteria'] = i
        else:
            filter = (df['Month_num'] == df['Month_num'].iloc[0]) & (df['Day'] == df['Day'].iloc[0])
            holder_dict['Criteria'] = i
        
        filtered_df = df[filter].loc[1:]

        min_first = filtered_df['first'].min()
        min_second = filtered_df['second'].min()
        min_third = filtered_df['third'].min()
        min_fourth = filtered_df['fourth'].min()
        min_fifth = filtered_df['fifth'].min()
        min_sixth = filtered_df['sixth'].min()

        max_first = filtered_df['first'].max()
        max_second = filtered_df['second'].max()
        max_third = filtered_df['third'].max()
        max_fourth = filtered_df['fourth'].max()
        max_fifth = filtered_df['fifth'].max()
        max_sixth = filtered_df['sixth'].max()

        if df['first'].iloc[0] >= filtered_df['first'].min() & df['first'].iloc[0] <= filtered_df['first'].max():
            holder_dict['first'] = 'Within'
        else:
            holder_dict['first'] = 'Out of Range'

        if df['second'].iloc[0] >= filtered_df['second'].min() & df['second'].iloc[0] <= filtered_df['second'].max():
            holder_dict['second'] = 'Within'
        else:
            holder_dict['second'] = 'Out of Range'

        if df['third'].iloc[0] >= filtered_df['third'].min() & df['third'].iloc[0] <= filtered_df['third'].max():
            holder_dict['third'] = 'Within'
        else:
            holder_dict['third'] = 'Out of Range'

        if df['fourth'].iloc[0] >= filtered_df['fourth'].min() & df['fourth'].iloc[0] <= filtered_df['fourth'].max():
            holder_dict['fourth'] = 'Within'
        else:
            holder_dict['fourth'] = 'Out of Range'

        if df['fifth'].iloc[0] >= filtered_df['fifth'].min() & df['fifth'].iloc[0] <= filtered_df['fifth'].max():
            holder_dict['fifth'] = 'Within'
        else:
            holder_dict['fifth'] = 'Out of Range'

        if df['sixth'].iloc[0] >= filtered_df['sixth'].min() & df['sixth'].iloc[0] <= filtered_df['sixth'].max():
            holder_dict['sixth'] = 'Within'
        else:
            holder_dict['sixth'] = 'Out of Range'
        
        rows.append(holder_dict)

    result_df = pd.DataFrame(rows)
    result_df = result_df[['Date', 'Winning Numbers', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'Criteria']]

    return result_df

def main():

    try:
        df_results = pd.read_excel(filename_all)
    except Exception as e:
        logger.error("Exception: " + str(e))
    else:
        logger.debug("Reading historical data")
    
    try:
        df_range = pd.read_excel(filename_range)
    except Exception as e:
        logger.error("Exception: " + str(e))
    else:
        logger.debug("Reading range records")
    
    latest_date       = df_results.loc[0, 'Date'].to_pydatetime().date()
    latest_date_range = df_range.loc[0, 'Date'].to_pydatetime().date()

    if latest_date_range == latest_date:
        logger.debug("Range output is aligned")
    else:
        logger.debug("Newer date detected: {}".format(str(latest_date)))
        new_range_df = checkRange(df_results)
        logger.debug("Generating new ranges")

        new_range_df = new_range_df.append(df_range, sort = False, ignore_index = True)
        new_range_df.to_excel(filename_range, index = False)
        logger.debug("Appended new ranges")

        print("done")

if __name__ == "__main__":
    main()