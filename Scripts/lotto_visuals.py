import pandas as pd
import numpy as np
import plotly.graph_objects as go
import chart_studio.plotly as py
import chart_studio
import logging

from plotly.subplots import make_subplots
from config import filename_excel, visual_log, day_type

## CHART STUDIO CONFIG
chart_studio.tools.set_credentials_file(username='rubberninja', api_key='FUPGqd08gWsRPq0PJP65')


## LOGGER CONFIG
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler(visual_log)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def histogram(df_new):
	## NUMBER LISTS
	first = list(df_new['first'])
	second = list(df_new['second'])
	third = list(df_new['third'])
	fourth = list(df_new['fourth'])
	fifth = list(df_new['fifth'])
	sixth = list(df_new['sixth'])
	
	## VISUALS
	fig = make_subplots(rows=3, cols=2, subplot_titles = ("First", "Second", "Third", "Fourth", "Fifth", "Sixth"), vertical_spacing=0.07)
	fig.add_trace(go.Histogram(x=first))
	fig.add_trace(go.Histogram(x=second), row = 1, col = 2)
	fig.add_trace(go.Histogram(x=third), row = 2, col = 1)
	fig.add_trace(go.Histogram(x=fourth), row = 2, col = 2)
	fig.add_trace(go.Histogram(x=fifth), row = 3, col = 1)
	fig.add_trace(go.Histogram(x=sixth), row = 3, col = 2)

	fig.update_xaxes(title_text = "Number", row = 1, col = 1)
	fig.update_xaxes(title_text = "Number", row = 1, col = 2)
	fig.update_xaxes(title_text = "Number", row = 2, col = 1)
	fig.update_xaxes(title_text = "Number", row = 2, col = 2)
	fig.update_xaxes(title_text = "Number", row = 3, col = 1)
	fig.update_xaxes(title_text = "Number", row = 3, col = 2)

	fig.update_yaxes(title_text = "Count", row = 1, col = 1)
	fig.update_yaxes(title_text = "Count", row = 1, col = 2)
	fig.update_yaxes(title_text = "Count", row = 2, col = 1)
	fig.update_yaxes(title_text = "Count", row = 2, col = 2)
	fig.update_yaxes(title_text = "Count", row = 3, col = 1)
	fig.update_yaxes(title_text = "Count", row = 3, col = 2)

	fig.update_layout( title_text = 'Lotto Histogram (6 months)', yaxis_title = 'count', xaxis_title = 'Numbers', height = 1200, width = 1200)

	py.plot(fig, filename = '6-42 Histogram', auto_open=True)
	
def line_graph(df_new):
	## VISUALS
    fig = make_subplots(rows=3, cols=2, subplot_titles = ("First", "Second", "Third", "Fourth", "Fifth", "Sixth"), vertical_spacing=0.07)
    
    fig.add_trace(go.Scatter(x = df_new['Date'], y = df_new['first'], name = "First Number", mode = "lines+markers", opacity = 0.8, legendgroup = "1st group"))
    fig.add_trace(go.Scatter(x = df_new['Date'], y = df_new['first_mean'], name = "Average", line_color = "#FF0000", mode = "lines", opacity = 0.6, legendgroup = "1st group"))
    
    fig.add_trace(go.Scatter(x = df_new['Date'], y = df_new['second'], name = "Second Number", mode = "lines+markers", opacity = 0.8, legendgroup = "2nd group"), row = 1, col = 2)
    fig.add_trace(go.Scatter(x = df_new['Date'], y = df_new['second_mean'], name = "Average", line_color = "#FF0000", mode = "lines", opacity = 0.6, legendgroup = "2nd group"),row = 1, col = 2)

    fig.add_trace(go.Scatter(x = df_new['Date'], y = df_new['third'], name = "Third Number",  mode = "lines+markers", opacity = 0.8, legendgroup = "3rd group"), row = 2, col = 1)
    fig.add_trace(go.Scatter(x = df_new['Date'], y = df_new['third_mean'], name = "Average", line_color = "#FF0000", mode = "lines", opacity = 0.6, legendgroup = "3rd group"),row = 2, col = 1)

    fig.add_trace(go.Scatter(x = df_new['Date'], y = df_new['fourth'], name = "Fourth Number", mode = "lines+markers", opacity = 0.8, legendgroup = "4th group"), row = 2, col = 2)
    fig.add_trace(go.Scatter(x = df_new['Date'], y = df_new['fourth_mean'], name = "Average", line_color = "#FF0000", mode = "lines", opacity = 0.6, legendgroup = "4th group"),row = 2, col = 2)

    fig.add_trace(go.Scatter(x = df_new['Date'], y = df_new['fifth'], name = "Fifth Number",  mode = "lines+markers", opacity = 0.8, legendgroup = "5th group"), row = 3, col = 1)
    fig.add_trace(go.Scatter(x = df_new['Date'], y = df_new['fifth_mean'], name = "Average", line_color = "#FF0000", mode = "lines", opacity = 0.6, legendgroup = "5th group"),row = 3, col = 1)

    fig.add_trace(go.Scatter(x = df_new['Date'], y = df_new['sixth'], name = "Sixth Number",  mode = "lines+markers", opacity = 0.8, legendgroup = "6th group"), row = 3, col = 2)
    fig.add_trace(go.Scatter(x = df_new['Date'], y = df_new['sixth_mean'], name = "Average", line_color = "#FF0000", mode = "lines", opacity = 0.6, legendgroup = "6th group"),row = 3, col = 2)
    
    fig.update_xaxes(title_text = "Date", row = 1, col = 1)
    fig.update_xaxes(title_text = "Date", row = 1, col = 2)
    fig.update_xaxes(title_text = "Date", row = 2, col = 1)
    fig.update_xaxes(title_text = "Date", row = 2, col = 2)
    fig.update_xaxes(title_text = "Date", row = 3, col = 1)
    fig.update_xaxes(title_text = "Date", row = 3, col = 2)
    
    fig.update_yaxes(title_text = "Digit", row = 1, col = 1)
    fig.update_yaxes(title_text = "Digit", row = 1, col = 2)
    fig.update_yaxes(title_text = "Digit", row = 2, col = 1)
    fig.update_yaxes(title_text = "Digit", row = 2, col = 2)
    fig.update_yaxes(title_text = "Digit", row = 3, col = 1)
    fig.update_yaxes(title_text = "Digit", row = 3, col = 2)
    
    fig.update_layout(title="Lotto Trends (6 months)", hovermode='x unified', font=dict(family="Helvetica"), height = 1200, width = 1200)
    
    py.plot(fig, filename = '6-42 Trends', auto_open=True)
    
def heatmap(df_new):
    ## GROUP BY
    df_grp = df_new.groupby('Day_Name')
    
    df_grp_first = pd.DataFrame({'value': df_grp['first'].value_counts()}).reset_index()
    df_grp_first['Day_Name'] = df_grp_first['Day_Name'].astype(day_type)
    df_grp_first = df_grp_first.sort_values(by=['Day_Name','first']).reset_index(drop=True)
    df_grp_first.rename(columns={"first": "key"},inplace=True)
    
    df_grp_second = pd.DataFrame({'value': df_grp['second'].value_counts()}).reset_index()
    df_grp_second['Day_Name'] = df_grp_second['Day_Name'].astype(day_type)
    df_grp_second = df_grp_second.sort_values(by=['Day_Name','second']).reset_index(drop=True)
    df_grp_second.rename(columns={"second": "key"},inplace=True)
    
    df_grp_third = pd.DataFrame({'value': df_grp['third'].value_counts()}).reset_index()
    df_grp_third['Day_Name'] = df_grp_third['Day_Name'].astype(day_type)
    df_grp_third = df_grp_third.sort_values(by=['Day_Name','third']).reset_index(drop=True)
    df_grp_third.rename(columns={"third": "key"},inplace=True)
    
    df_grp_fourth = pd.DataFrame({'value': df_grp['fourth'].value_counts()}).reset_index()
    df_grp_fourth['Day_Name'] = df_grp_fourth['Day_Name'].astype(day_type)
    df_grp_fourth = df_grp_fourth.sort_values(by=['Day_Name','fourth']).reset_index(drop=True)
    df_grp_fourth.rename(columns={"fourth": "key"},inplace=True)

    df_grp_fifth = pd.DataFrame({'value': df_grp['fifth'].value_counts()}).reset_index()
    df_grp_fifth['Day_Name'] = df_grp_fifth['Day_Name'].astype(day_type)
    df_grp_fifth = df_grp_fifth.sort_values(by=['Day_Name','fifth']).reset_index(drop=True)
    df_grp_fifth.rename(columns={"fifth": "key"},inplace=True)

    df_grp_sixth = pd.DataFrame({'value': df_grp['sixth'].value_counts()}).reset_index()
    df_grp_sixth['Day_Name'] = df_grp_sixth['Day_Name'].astype(day_type)
    df_grp_sixth = df_grp_sixth.sort_values(by=['Day_Name','sixth']).reset_index(drop=True)
    df_grp_sixth.rename(columns={"sixth": "key"},inplace=True)
    
    ## MERGE
    df_combine = pd.concat([df_grp_first, df_grp_second]).groupby(["Day_Name","key"], as_index = False)["value"].sum()
    df_combine = df_combine.dropna(subset=['value']).reset_index(drop=True)
    df_combine['value'] = df_combine['value'].astype(int)

    df_combine = pd.concat([df_combine, df_grp_third]).groupby(["Day_Name","key"], as_index = False)["value"].sum()
    df_combine = df_combine.dropna(subset=['value']).reset_index(drop=True)
    df_combine['value'] = df_combine['value'].astype(int)

    df_combine = pd.concat([df_combine, df_grp_fourth]).groupby(["Day_Name","key"], as_index = False)["value"].sum()
    df_combine = df_combine.dropna(subset=['value']).reset_index(drop=True)
    df_combine['value'] = df_combine['value'].astype(int)

    df_combine = pd.concat([df_combine, df_grp_fifth]).groupby(["Day_Name","key"], as_index = False)["value"].sum()
    df_combine = df_combine.dropna(subset=['value']).reset_index(drop=True)
    df_combine['value'] = df_combine['value'].astype(int)

    df_combine = pd.concat([df_combine, df_grp_sixth]).groupby(["Day_Name","key"], as_index = False)["value"].sum()
    df_combine = df_combine.dropna(subset=['value']).reset_index(drop=True)
    df_combine['value'] = df_combine['value'].astype(int)
    
    ## MERGE FILLERS
    day_fill = np.array(['Tuesday','Thursday','Saturday'])
    day_fill = np.repeat(day_fill,42)
    day_fill = list(day_fill)

    key_fill = np.linspace(1, 42, num = 42)
    key_fill = np.tile(key_fill, 3)
    key_fill = list(map(int, list(key_fill)))

    value_fill = [x * 0 for x in range(42*3)]

    df_fill = pd.DataFrame({'Day_Name': day_fill, 'key': key_fill, 'value': value_fill})

    df_combine = pd.concat([df_combine, df_fill]).groupby(["Day_Name","key"], as_index = False)["value"].sum()
    df_combine = df_combine.dropna(subset=['value']).reset_index(drop=True)
    df_combine['value'] = df_combine['value'].astype(int)
    
    ## SETTING PARAMETERS
    filt_tues = df_combine['Day_Name'] == 'Tuesday'
    list_tues = df_combine[filt_tues]['value'].tolist()

    filt_thurs = df_combine['Day_Name'] == 'Thursday'
    list_thurs = df_combine[filt_thurs]['value'].tolist()

    filt_sat = df_combine['Day_Name'] == 'Saturday'
    list_sat = df_combine[filt_sat]['value'].tolist()

    z = []
    z.append(list_tues)
    z.append(list_thurs)
    z.append(list_sat)
    
    ## VISUALS
    fig = go.Figure(data = go.Heatmap(
                z = z,
                x = list(np.linspace(1,42,num=42)),
                y = ['Tuesday','Thursday','Saturday'],
                hoverongaps = False,
                colorscale = 'Hot',
                reversescale = True))

    fig.update_layout( title_text = 'Lotto Heatmap (6 months)', yaxis_title = 'Day of Result', xaxis_title = 'Single Lotto Digit')

    py.plot(fig, filename = '6-42 Heatmap', auto_open=True)

def main():
    try:
        df = pd.read_excel(filename_excel)
    except Exception as e:
        logger.critical("Exception: " + str(e))
    else:
        logger.debug("Reading historical data")
        
    df.drop(columns=['Unnamed: 0'], inplace=True)
    
    ## DATA TRANSFORMATION
    logger.debug("Data Transformation")
    
    df['Date'] = pd.to_datetime(df['Date'], format = '%d/%m/%Y')
    df['Day_Name'] = df['Date'].dt.day_name()
    
    logger.debug("Filtering past 6 months")
    
    filt = df['Date'] >= df['Date'].max() - pd.DateOffset(months=6)
    df_year = df[filt]
    df_new = df_year.copy()
    
    df_new['first_mean'] = df_new['first'].mean()
    df_new['second_mean'] = df_new['second'].mean()
    df_new['third_mean'] = df_new['third'].mean()
    df_new['fourth_mean'] = df_new['fourth'].mean()
    df_new['fifth_mean'] = df_new['fifth'].mean()
    df_new['sixth_mean'] = df_new['sixth'].mean()
	
    try:
        line_graph(df_new)
    except Exception as e:
        logger.critical("Exception: " + str(e))
    else:
        logger.debug("Creating line graphs")
        
    try:
        heatmap(df_new)
    except Exception as e:
        logger.critical("Exception: " + str(e))
    else:
        logger.debug("Creating heatmap")
	
    try:
        histogram(df_new)
    except Exception as e:
        logger.critical("Exception: " + str(e))
    else:
        logger.debug("Creating histograms")

if __name__ == "__main__":
    main()