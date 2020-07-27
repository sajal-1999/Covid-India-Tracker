import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# import plotly.graph_objects as go
# # import plotly.express as px

from get_data import *
from totalgraph import india_graph
from navbar import navbar, new_navbar
from total_stats import cards

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app.title = "Covid India Tracker"

state_list = []
for i in get_state_list():
    state_list.append(dbc.DropdownMenuItem(i))

district_list = []
state_name = 'Maharashtra' #Kept static for now. Need to fetch from state drop-down
for i in get_state_to_district_mapping(state_name):
    district_list.append(dbc.DropdownMenuItem(i))


top_row = dbc.Container([
    dbc.Row([cards, india_graph]),
    dbc.Row([
        dbc.DropdownMenu(
            label="Select State", id="state-selected", children=state_list, className="mb-3", right=True
        ),
        dbc.DropdownMenu(
            label="Select District", id="district-selected", children=district_list, className="mb-3", right=True
        ),
    ], no_gutters=False,),
    # dbc.Row([state graph])
])


app.layout = html.Div(#style={'backgroundColor': 'black'},
    children=[
        new_navbar,
        html.Br(),
        # cards,
        top_row,
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



# @app.callback(
#     Output("district-selected", "children"),
#     [Input("state-selected", "")]
# )
# def update_district():