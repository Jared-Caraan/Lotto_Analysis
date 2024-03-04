# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc, Input, Output, callback
from config import filename_all, visual_log, day_type
from collections import Counter

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import math

def getMean(series):
    
    sum = 0
    lst = series.to_list()
    for i,x in Counter(lst).items():
        sum += i * (x / len(lst))
    
    return sum

def getStdev(series):

    mean = 0
    lst = series.to_list()
    for i,x in Counter(lst).items():
        mean += i * (x / len(lst))
    
    sum = 0
    for i,x in Counter(lst).items():
        sum += (i**2) * (x / len(lst))
    
    return math.sqrt(sum - (mean**2))

app = Dash(__name__)

colors = {
    'background': '#282A35',
    'text': 'white'
}

df = pd.read_excel(filename_all)
df = df.rename(columns = {'Winning Numbers': 'Draw'})
df['Year'] = df['Date'].dt.strftime('%Y')
df['Month'] = df['Date'].dt.strftime('%B')
df['Month_num'] = df['Date'].dt.strftime('%m').str.lstrip("0")
df['Day'] = df['Date'].dt.strftime('%d')
df['Day'] = df['Day'].str.lstrip("0")

trace1 = go.Indicator(
    mode = "number",
    value = 0,
    delta = {"reference": 0, "valueformat": ".3f"},
    title = {"text": "First number"},
    number = {'font':{'size': 50}},
    domain = {'x': [0, 0.2], 'y': [0.8, 1]})

trace2 = go.Indicator(
    mode = "number",
    value = 0,
    delta = {"reference": 0, "valueformat": ".3f"},
    title = {"text": "Second number"},
    number = {'font':{'size': 50}},
    domain = {'x': [0, 1], 'y': [0.8, 1]})

trace3 = go.Indicator(
    mode = "number",
    value = 0,
    delta = {"reference": 0, "valueformat": ".3f"},
    title = {"text": "Third number"},
    number = {'font':{'size': 50}},
    domain = {'x': [0.8, 1], 'y': [0.8, 1]})

trace4 = go.Indicator(
    mode = "number",
    value = 0,
    delta = {"reference": 0, "valueformat": ".3f"},
    title = {"text": "Fourth number"},
    number = {'font':{'size': 50}},
    domain = {'x': [0, 0.2], 'y': [0, 1]})

trace5 = go.Indicator(
    mode = "number",
    value = 0,
    delta = {"reference": 0, "valueformat": ".3f"},
    title = {"text": "Fifth number"},
    number = {'font':{'size': 50}},
    domain = {'x': [0, 1], 'y': [0, 1]})

trace6 = go.Indicator(
    mode = "number",
    value = 0,
    delta = {"reference": 0, "valueformat": ".3f"},
    title = {"text": "Sixth number"},
    number = {'font':{'size': 50}},
    domain = {'x': [0.8, 1], 'y': [0, 1]})

trace7 = go.Indicator(
    mode = "number",
    value = 22,
    delta = {"reference": 0, "valueformat": ".3f"},
    title = {"text": "Record Count"},
    number = {'font':{'size': 50}},
    domain = {'x': [0, 0.2], 'y': [0, 0.2]})

fig = go.FigureWidget(data=[trace1,trace2,trace3,trace4,trace5,trace6,trace7],
                         layout=go.Layout(
                            title=dict(
                                text='Six Numbers EDA'
                            )))

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor='blue',
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': '#282A35'}, children=[
    html.H1(children='Probability Distribution Analysis',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }),
    html.Br(),
    html.P(children='''
        The values below shows the central tendency and range of all the 6/42 results per digit. It is also important to note that the results extracted are arranged in numerical order.
    ''', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    html.Hr(),html.Br(), html.Br(),
    html.Div(className = "eda-help-panel-div",
        children = [
            html.Li(children='''
                Use Date - When checked, it enables the second widget (day and month number) to be chosen. This will disable the day name to be clicked.
                '''),
            html.Br(),
            html.Li(children='''
                Month & Day Number - This allows you to pick a specific month and day number. This is only allowed when Use Data widget is ticked.
                '''),
            html.Br(),
            html.Li(children='''
                Day Name & Stat Function - This allows you to pick the day name. The day name refers to the day when a result is generated. The Stat Function refers to what statistical function would you like to use to describe the data.
                ''')
        ]
    ),
    html.Br(), html.Br(),
    html.Div([

        html.Div([
            dcc.Checklist(
                ['Use Date'],
                id='check-date', 
                style={'color':'white'}
            )
        ]),

        html.Div(className = "eda-widgets-div", children=[
            html.Span("Month Number", style={'color':'white', "position":"absolute","top":"10px"}),
            html.Div([
            dcc.Dropdown(
                [i for i in range(1,13)],
                1,
                id='drop-month'
            )], style={"position":"absolute", "top":"35px", "width":"93.5%"}),
            html.Span("Day Number", style={'color':'white', "position":"absolute","bottom":"50px"}),
            html.Div([
            dcc.Dropdown(
                [i for i in range(1,32)],
                1,
                id='drop-day'
            )], style={"position":"absolute", "bottom":"10px", "width":"93.5%"})
        ]),

        html.Div(className = "eda-widgets-div", children = [
            html.Span("Day Name", style={'color':'white', "position":"absolute","top":"10px"}),
            html.Div([
            dcc.Dropdown(
                list(df['Day_Name'].unique()),
                'Thursday',
                id='drop-day_name'
            )], style={"position":"absolute", "top":"35px", "width":"93.5%"}),
            html.Span("Stat Function", style={'color':'white', "position":"absolute","bottom":"50px"}),
            html.Div([
            dcc.Dropdown(
                ['Mean', 'Standard Deviation'],
                'Mean',
                id='drop-stat_func'
            )], style={"position":"absolute", "bottom":"10px", "width":"93.5%"})
        ]),

    ], style={"display":"flex", "padding":"20px", "justify-content":"space-evenly"}),
    html.Hr(),
    html.Div([
        dcc.Graph(
            id='example-graph',
            figure=fig
        )])
])

@callback(
    Output('drop-month', 'disabled'),
    Output('drop-day', 'disabled'),
    Input('check-date', 'value')
)
def use_date_disable_day(toggle):
    if not toggle:
        return True, True
    return False, False

@callback(
    Output('drop-day_name', 'disabled'),
    Input('check-date', 'value')
)
def use_date_enable(toggle):
    if toggle:
        return True
    return False

@callback(
    Output('example-graph', 'figure'),
    Input('check-date', 'value'),
    Input('drop-month', 'value'),
    Input('drop-day', 'value'),
    Input('drop-day_name', 'value'),
    Input('drop-stat_func', 'value')
)
def update_figure(toggle_date, selected_month, selected_day, selected_day_name, selected_func):
    if toggle_date:
        filter_list = [i and j for i, j in
                        zip(df['Month_num'] == str(selected_month), df['Day'] == str(selected_day))]
        temp_df = df[filter_list]
    else:
        temp_df = df[df['Day_Name'] == selected_day_name]

    if selected_func == 'Mean':
        try:

            temp_first  = getMean(temp_df['first'])
            temp_second = getMean(temp_df['second'])
            temp_third  = getMean(temp_df['third'])
            temp_fourth = getMean(temp_df['fourth'])
            temp_fifth  = getMean(temp_df['fifth'])
            temp_sixth  = getMean(temp_df['sixth'])
        except:
            temp_first, temp_second, temp_third, temp_fourth, temp_fifth, temp_sixth  = 0,0,0,0,0,0
    elif selected_func == 'Standard Deviation':
        try:
            temp_first  = getStdev(temp_df['first'])
            temp_second = getStdev(temp_df['second'])
            temp_third  = getStdev(temp_df['third'])
            temp_fourth = getStdev(temp_df['fourth'])
            temp_fifth  = getStdev(temp_df['fifth'])
            temp_sixth  = getStdev(temp_df['sixth'])
        except:
            temp_first, temp_second, temp_third, temp_fourth, temp_fifth, temp_sixth  = 0,0,0,0,0,0
    
    trace1 = go.Indicator(
        mode = "number",
        value = temp_first,
        delta = {"reference": 0, "valueformat": ".3f"},
        title = {"text": "First number"},
        number = {'font':{'size': 50}},
        domain = {'x': [0, 0.2], 'y': [0.8, 1]})
    
    trace2 = go.Indicator(
        mode = "number",
        value = temp_second,
        delta = {"reference": 0, "valueformat": ".3f"},
        title = {"text": "Second number"},
        number = {'font':{'size': 50}},
        domain = {'x': [0, 1], 'y': [0.8, 1]})

    trace3 = go.Indicator(
        mode = "number",
        value = temp_third,
        delta = {"reference": 0, "valueformat": ".3f"},
        title = {"text": "Third number"},
        number = {'font':{'size': 50}},
        domain = {'x': [0.8, 1], 'y': [0.8, 1]})

    trace4 = go.Indicator(
        mode = "number",
        value = temp_fourth,
        delta = {"reference": 0, "valueformat": ".3f"},
        title = {"text": "Fourth number"},
        number = {'font':{'size': 50}},
        domain = {'x': [0, 0.2], 'y': [0, 1]})

    trace5 = go.Indicator(
        mode = "number",
        value = temp_fifth,
        delta = {"reference": 0, "valueformat": ".3f"},
        title = {"text": "Fifth number"},
        number = {'font':{'size': 50}},
        domain = {'x': [0, 1], 'y': [0, 1]})

    trace6 = go.Indicator(
        mode = "number",
        value = temp_sixth,
        delta = {"reference": 0, "valueformat": ".3f"},
        title = {"text": "Sixth number"},
        number = {'font':{'size': 50}},
        domain = {'x': [0.8, 1], 'y': [0, 1]})

    trace7 = go.Indicator(
        mode = "number",
        value = len(temp_df),
        delta = {"reference": 0, "valueformat": ".3f"},
        title = {"text": "Record Count"},
        number = {'font':{'size': 50}},
        domain = {'x': [0, 0.2], 'y': [0, 0.2]})

    fig = go.FigureWidget(data=[trace1,trace2,trace3,trace4,trace5,trace6,trace7],
                         layout=go.Layout(
                            title=dict(
                                text='Six Numbers EDA'
                            )))
    
    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)
