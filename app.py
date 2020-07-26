import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
# import plotly.express as px
from get_data import get_data, get_state_list_options
from totalgraph import india_graph

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app.title = "Covid India Tracker"

body = dbc.Container([
    dbc.Row([india_graph])
])


app.layout = html.Div(#style={'backgroundColor': 'black'},
    children=[
    html.H1('Hello user', style = {'textAlign': 'center', 'color': 'red'}),
    html.Div(children = '''
        Dash: A web application framework for Python.
    '''),
    dcc.Graph(
        id = 'example-graph',
        # figure = get_graph
    ),
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=get_state_list_options(),
        value='AN'
    )
])

if __name__ == '__main__':
    app.run_server(dev_tools_hot_reload=True, debug=True)
