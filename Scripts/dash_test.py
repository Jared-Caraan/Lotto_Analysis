# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc, Input, Output, callback
from config import filename_all, visual_log, day_type

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {
    'background': '#F3F5F9',
    'text': 'black'
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
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children='Hello Dashes',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }),

    html.Div(children='''
        Dash: A web application framework for your data.
    ''', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    html.Div([

        html.Div([
            dcc.Checklist(
                ['Use Date'],
                id='check-date', 
                style={'color':'black'}
            )
        ]),

        html.Div([
            html.Span("MONTH & DAY"),
            html.Div([
            dcc.Dropdown(
                [i for i in range(1,13)],
                1,
                id='drop-month'
            )], style={}),

            html.Div([
            dcc.Dropdown(
                [i for i in range(1,32)],
                1,
                id='drop-day'
            )], style={"margin-top":"20px"})
        ], style={"width":"20%", "padding":"10px", "border-radius":"3px", "background-color":"white", "position":"relative", "border-bottom":"5px solid red"}),

        html.Div([
            html.Span("DAY NAME & STAT FUNCTION", style={"margin-bottom":"5px"}),
            html.Div([
            dcc.Dropdown(
                list(df['Day_Name'].unique()),
                'Thursday',
                id='drop-day_name'
            )]),

            # html.Label('Central Tendency', style={'color':'white'}),
            html.Div([
            dcc.Dropdown(
                ['Mean', 'Median', 'Max', 'Min'],
                'Mean',
                id='drop-stat_func'
            )], style={"position":"absolute", "bottom":"8px", "right": "10px", "width":"93.5%"})

        ], style={"width":"20%", "padding":"10px", "border-radius":"3px", "background-color":"white", "position":"relative", "border-bottom":"5px solid blue"})

    ], style={"display":"flex", "padding":"20px", "justify-content":"space-evenly"}),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
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
        temp_first  = temp_df['first'].mean()
        temp_second = temp_df['second'].mean()
        temp_third  = temp_df['third'].mean()
        temp_fourth = temp_df['fourth'].mean()
        temp_fifth  = temp_df['fifth'].mean()
        temp_sixth  = temp_df['sixth'].mean()
    elif selected_func == 'Median':
        temp_first  = temp_df['first'].median()
        temp_second = temp_df['second'].median()
        temp_third  = temp_df['third'].median()
        temp_fourth = temp_df['fourth'].median()
        temp_fifth  = temp_df['fifth'].median()
        temp_sixth  = temp_df['sixth'].median()
    elif selected_func == 'Max':
        temp_first = temp_df['first'].max()
        temp_second = temp_df['second'].max()
        temp_third  = temp_df['third'].max()
        temp_fourth = temp_df['fourth'].max()
        temp_fifth  = temp_df['fifth'].max()
        temp_sixth  = temp_df['sixth'].max()
    elif selected_func == 'Min':
        temp_first = temp_df['first'].min()
        temp_second = temp_df['second'].min()
        temp_third  = temp_df['third'].min()
        temp_fourth = temp_df['fourth'].min()
        temp_fifth  = temp_df['fifth'].min()
        temp_sixth  = temp_df['sixth'].min()
    
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
