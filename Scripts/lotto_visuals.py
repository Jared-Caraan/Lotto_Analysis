import chart_studio.plotly as py
import plotly.graph_objects as go

trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 20]
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 25]
)

data = [trace0, trace1]

py.plot(data, filename = 'My Second Graph', auto_open = True)