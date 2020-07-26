import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from get_data import get_data

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

fig = px.line(get_data(), x = 'Date', y=['Total Confirmed', 'Total Recovered', 'Total Deceased'])

app.layout = html.Div(children=[
    html.H1('Hello user', style = {'textAlign': 'center', 'color': 'red'}),
    html.Div(children = '''
        Dash: A web application framework for Python.
    '''),
    dcc.Graph(
        id = 'example-graph',
        figure = fig
    )
])

if __name__ == '__main__':
    app.run_server(dev_tools_hot_reload=True, debug=True)