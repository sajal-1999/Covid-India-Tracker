import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
# import plotly.express as px
from get_data import get_data, get_state_list_options, get_state_list
from totalgraph import india_graph
from navbar import navbar, new_navbar
from total_stats import cards

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app.title = "Covid India Tracker"

body = dbc.Container([
    dbc.Row([india_graph]),
    # dbc.Row([choose_state, choose_district]),
    # dbc.Row([state graph, district_graph])
])

items = []
for i in get_state_list():
    items.append(dbc.DropdownMenuItem(i))

app.layout = html.Div(#style={'backgroundColor': 'black'},
    children=[
    new_navbar,
    html.Br(),
    cards,
    body,
    html.Label('Dropdown'),
    # dcc.Dropdown(
    #     options=get_state_list_options(),
    #     value='AN',
    #     style = {'color': 'black', 'text': 'white'}
    # )
    dbc.DropdownMenu(
            label="Choose state", children=items, className="mb-3", right=True
        ),
])

if __name__ == '__main__':
    app.run_server(dev_tools_hot_reload=True, debug=True)

@app.callback(
    Output("registeration-toast", "is_open"),
    [Input("sign-up-button", "n_clicks")],
)
def open_toast(n):
    if n:
        return True
    return False