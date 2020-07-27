import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
# import plotly.express as px
from get_data import get_data, get_state_list_options
from totalgraph import india_graph
from navbar import navbar, new_navbar
from total_stats import cards

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app.title = "Covid India Tracker"

body = dbc.Container([
    dbc.Row([india_graph]),
    # dbc.Row([choose_state, choose_district]),
    # dbc.Row([district_graph])
])

# items = []
# for i in get_state_list_options():
#     items.append(dbc.DropdownMenuItem(i))

app.layout = html.Div(#style={'backgroundColor': 'black'},
    children=[
    new_navbar,
    dbc.Row([html.Br()]),
    cards,
#   total_stats

    # html.H1('Hello user', style = {'textAlign': 'center', 'color': 'red'}),
    # html.Div(children = '''
    #     Dash: A web application framework for Python.
    # '''),
    body,
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=get_state_list_options(),
        value='AN',
        style = {'color': 'black', 'text': 'white'}
    )
    # dbc.DropdownMenu(
    #         label="Choose state", children=items, className="mb-3"
    #     ),
])

if __name__ == '__main__':
    app.run_server(dev_tools_hot_reload=True, debug=True)

@app.callback(
    Output("registeration-toast", "is_open"),
    [Input("sign-up-button", "n_clicks")],
)
def open_toast(n=1):
    if n:
        return True
    return False