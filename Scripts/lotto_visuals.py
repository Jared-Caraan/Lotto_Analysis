import pandas as pd
import plotly.graph_objects as go
import chart_studio.plotly as py

from plotly.subplots import make_subplots
from config import filename_excel


def main():
    df = pd.read_excel(filename_excel)
    df.drop(columns=['Unnamed: 0'], inplace=True)
    
    ##DATA TRANSFORMATION
    df['Date'] = pd.to_datetime(df['Date'], format = '%d/%m/%Y')
    df['Day_Name'] = df['Date'].dt.day_name()
    
    ##NEW DATAFRAME
    filt = df['Date'] >= df['Date'].max() - pd.DateOffset(months=6)
    df_year = df[filt]
    df_new = df_year.copy()
    
    df_new['first_mean'] = df_new['first'].mean()
    df_new['second_mean'] = df_new['second'].mean()
    df_new['third_mean'] = df_new['third'].mean()
    df_new['fourth_mean'] = df_new['fourth'].mean()
    df_new['fifth_mean'] = df_new['fifth'].mean()
    df_new['sixth_mean'] = df_new['sixth'].mean()
    
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
    
    fig.update_layout(title="6/42 winning numbers for the past 6 months", hovermode='x unified', font=dict(family="Helvetica"), height = 1200, width = 1200)
    
    py.plot(fig, filename = '6-42 Dashboard', auto_open=True)

if __name__ == "__main__":
    main()