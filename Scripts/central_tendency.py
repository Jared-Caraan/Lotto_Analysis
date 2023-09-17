import plotly.graph_objects as go
import chart_studio.plotly as py

from ipywidgets import widgets

def visual_eda_col(df):
    month_num_list = list(df['Month_num'].unique().astype(int))
    day_list = list(df['Day'].unique().astype(int))

    month_num_list.sort()
    day_list.sort()

    month = widgets.Dropdown(
        options=month_num_list,
        value = 1,
        description='Month:',
    )

    day = widgets.Dropdown(
        options=day_list,
        value = 1,
        description='Day:',
    )

    use_date = widgets.Checkbox(
        description='Date: ',
        value=True,
    )

    container = widgets.HBox(children=[use_date, month, day])

    day_name = widgets.Dropdown(
        options=list(df['Day_Name'].unique()),
        value='Thursday',
        description='Day Name:',
    )

    stat_func = widgets.Dropdown(
        options=['Mean', 'Median', 'Mode', 'Max', 'Min'],
        value='Mean',
        description='Function:',
    )


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
    
    def response(change):
        if use_date.value:
            filter_list = [i and j for i, j in
                           zip(df['Month_num'] == str(month.value), df['Day'] == str(day.value))]
            temp_df = df[filter_list]
        else:
            temp_df = df[df['Day_Name'] == day_name.value]

        if stat_func.value == 'Mean':
            temp_first  = temp_df['first'].mean()
            temp_second = temp_df['second'].mean()
            temp_third  = temp_df['third'].mean()
            temp_fourth = temp_df['fourth'].mean()
            temp_fifth  = temp_df['fifth'].mean()
            temp_sixth  = temp_df['sixth'].mean()
        elif stat_func.value == 'Median':
            temp_first  = temp_df['first'].median()
            temp_second = temp_df['second'].median()
            temp_third  = temp_df['third'].median()
            temp_fourth = temp_df['fourth'].median()
            temp_fifth  = temp_df['fifth'].median()
            temp_sixth  = temp_df['sixth'].median()
        elif stat_func.value == 'Mode':
            temp_first  = temp_df['first'].mode()[0]
            temp_second = temp_df['second'].mode()[0]
            temp_third  = temp_df['third'].mode()[0]
            temp_fourth = temp_df['fourth'].mode()[0]
            temp_fifth  = temp_df['fifth'].mode()[0]
            temp_sixth  = temp_df['sixth'].mode()[0]
        elif stat_func.value == 'Max':
            temp_first = temp_df['first'].max()
            temp_second = temp_df['second'].max()
            temp_third  = temp_df['third'].max()
            temp_fourth = temp_df['fourth'].max()
            temp_fifth  = temp_df['fifth'].max()
            temp_sixth  = temp_df['sixth'].max()
        elif stat_func.value == 'Min':
            temp_first = temp_df['first'].min()
            temp_second = temp_df['second'].min()
            temp_third  = temp_df['third'].min()
            temp_fourth = temp_df['fourth'].min()
            temp_fifth  = temp_df['fifth'].min()
            temp_sixth  = temp_df['sixth'].min()

        with fig.batch_update():
            fig.data[0].value = temp_first
            fig.data[1].value = temp_second
            fig.data[2].value = temp_third
            fig.data[3].value = temp_fourth
            fig.data[4].value = temp_fifth
            fig.data[5].value = temp_sixth
            fig.data[6].value = len(temp_df)


    month.observe(response, names="value")
    day.observe(response, names="value")
    use_date.observe(response, names="value")
    day_name.observe(response, names="value")
    stat_func.observe(response, names="value")
    
    container2 = widgets.HBox([day_name, stat_func])

    py.plot(fig, auto_open=True, sharing='public')
    return widgets.VBox([container,
                  container2,
                  fig])