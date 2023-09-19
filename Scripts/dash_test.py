# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

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
    value = 0,
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
        dcc.Checklist(
            ['Use Date'],
            id='check-date', 
            style={'color':'white'}
        ),

        html.Br(),
        html.Label('Month', style={'color':'white'}),
        dcc.Dropdown(
            [i for i in range(1,13)],
            1,
            id='drop-month'
        ),

        html.Br(),
        html.Label('Day', style={'color':'white'}),
        dcc.Dropdown(
            [i for i in range(1,32)],
            1,
            id='drop-day'
        )

    ], style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        html.Label('Day Name', style={'color':'white'}),
        dcc.Dropdown(
            ['Friday', 'Thursday', 'Saturday'],
            'Thursday',
            id='drop-day_name'
        ),

        html.Br(),
        html.Label('Central Tendency', style={'color':'white'}),
        dcc.Dropdown(
            ['Mean', 'Median', 'Mode', 'Max', 'Min'],
            'Mean',
            id='drop-stat_func'
        )

    ], style={'width': '45%', 'display': 'inline-block'}),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
