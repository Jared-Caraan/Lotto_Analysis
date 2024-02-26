# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc, Input, Output, callback, dash_table
from config import filename_all, visual_log, day_type

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import math

app = Dash(__name__)

colors = {
    'background': '#282A35',
    'text': 'white'
}

def putRemark(df, basis_df, result_df):
    if df['first'].iloc[0] >= basis_df['first'].min() & df['first'].iloc[0] <= basis_df['first'].max():
        result_df['first'] = 'Within'
    else:
        result_df['first'] = 'Out of Range'

    if df['second'].iloc[0] >= basis_df['second'].min() & df['second'].iloc[0] <= basis_df['second'].max():
        result_df['second'] = 'Within'
    else:
        result_df['second'] = 'Out of Range'

    if df['third'].iloc[0] >= basis_df['third'].min() & df['third'].iloc[0] <= basis_df['third'].max():
        result_df['third'] = 'Within'
    else:
        result_df['third'] = 'Out of Range'

    if df['fourth'].iloc[0] >= basis_df['fourth'].min() & df['fourth'].iloc[0] <= basis_df['fourth'].max():
        result_df['fourth'] = 'Within'
    else:
        result_df['fourth'] = 'Out of Range'

    if df['fifth'].iloc[0] >= basis_df['fifth'].min() & df['fifth'].iloc[0] <= basis_df['fifth'].max():
        result_df['fifth'] = 'Within'
    else:
        result_df['fifth'] = 'Out of Range'

    if df['sixth'].iloc[0] >= basis_df['sixth'].min() & df['sixth'].iloc[0] <= basis_df['sixth'].max():
        result_df['sixth'] = 'Within'
    else:
        result_df['sixth'] = 'Out of Range'
    
    return result_df

df = pd.read_excel(filename_all)
df = df.rename(columns = {'Winning Numbers': 'Draw'})
df['Year'] = df['Date'].dt.strftime('%Y')
df['Month'] = df['Date'].dt.strftime('%B')
df['Month_num'] = df['Date'].dt.strftime('%m').str.lstrip("0")
df['Day'] = df['Date'].dt.strftime('%d')
df['Day'] = df['Day'].str.lstrip("0")
df_latest = df.head(1)
df_latest = df_latest[['Date', 'Draw', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'Day_Name', 'Month_num', 'Day']]

day_name_latest = df_latest['Day_Name'].iloc[0]
month_latest = df_latest['Month_num'].iloc[0]
day_latest = df_latest['Day'].iloc[0]

basis_filter_1 = df['Day_Name'] == day_name_latest
basis_df_day_name = df[basis_filter_1].loc[1:]

min_day_name_first = basis_df_day_name['first'].min()
min_day_name_second = basis_df_day_name['second'].min()
min_day_name_third = basis_df_day_name['third'].min()
min_day_name_fourth = basis_df_day_name['fourth'].min()
min_day_name_fifth = basis_df_day_name['fifth'].min()
min_day_name_sixth = basis_df_day_name['sixth'].min()

max_day_name_first = basis_df_day_name['first'].max()
max_day_name_second = basis_df_day_name['second'].max()
max_day_name_third = basis_df_day_name['third'].max()
max_day_name_fourth = basis_df_day_name['fourth'].max()
max_day_name_fifth = basis_df_day_name['fifth'].max()
max_day_name_sixth = basis_df_day_name['sixth'].max()

result_df_day_name = df_latest[['Date', 'Draw']]

result_df_day_name = putRemark(df_latest, basis_df_day_name, result_df_day_name)
result_df_day_name['Criteria'] = 'Day Name'

basis_filter_2 = (df['Month_num'] == month_latest) & (df['Day'] == day_latest)
basis_df_month_day = df[basis_filter_2].loc[1:]

min_month_day_first = basis_df_month_day['first'].min()
min_month_day_second = basis_df_month_day['second'].min()
min_month_day_third = basis_df_month_day['third'].min()
min_month_day_fourth = basis_df_month_day['fourth'].min()
min_month_day_fifth = basis_df_month_day['fifth'].min()
min_month_day_sixth = basis_df_month_day['sixth'].min()

max_month_day_first = basis_df_month_day['first'].max()
max_month_day_second = basis_df_month_day['second'].max()
max_month_day_third = basis_df_month_day['third'].max()
max_month_day_fourth = basis_df_month_day['fourth'].max()
max_month_day_fifth = basis_df_month_day['fifth'].max()
max_month_day_sixth = basis_df_month_day['sixth'].max()

result_df_month_day = df_latest[['Date', 'Draw']]

result_df_month_day = putRemark(df_latest, basis_df_month_day, result_df_month_day)
result_df_month_day['Criteria'] = 'Month-Day'

app.layout = html.Div(style={'backgroundColor': '#282A35'}, children=[
    html.H1(children='Out of Range Checker',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }),
    html.Br(),
    html.P(children='''
        The information below shows if the latest result falls within the minimum and maximum values of a specific time criteria.
    ''', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    html.Hr(),html.Br(), html.Br(),
    html.Div([
    html.H4('Latest Result Table'),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} 
                    for i in df_latest.columns],
            data=df_latest.to_dict('records'),
            style_cell=dict(textAlign='left'),
            style_header=dict(backgroundColor="paleturquoise"),
            style_data=dict(backgroundColor="lavender")
        ), 
    ]),
    html.Hr(),html.Br(), html.Br(),
    html.Div([
    html.H4('Result Table for {}'.format(day_name_latest)),
        dash_table.DataTable(
            id='result_table_day_name',
            columns=[{"name": i, "id": i} 
                    for i in result_df_day_name.columns],
            data=result_df_day_name.to_dict('records'),
            style_cell=dict(textAlign='left'),
            style_header=dict(backgroundColor="paleturquoise"),
            style_data=dict(backgroundColor="lavender")
        ), 
    ]),
    html.Hr(),html.Br(), html.Br(),
    html.Div([
    html.H4('Result Table for {}-{}'.format(month_latest,day_latest)),
        dash_table.DataTable(
            id='result_table_month_day',
            columns=[{"name": i, "id": i} 
                    for i in result_df_month_day.columns],
            data=result_df_month_day.to_dict('records'),
            style_cell=dict(textAlign='left'),
            style_header=dict(backgroundColor="paleturquoise"),
            style_data=dict(backgroundColor="lavender")
        ), 
    ])
])

if __name__ == '__main__':
    app.run(debug=True)
