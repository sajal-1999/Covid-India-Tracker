import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
# # import plotly.express as px

from get_data import *
from totalgraph import india_graph
from navbar import new_navbar
from total_stats import cards
from select_graph_att import state_dcc, district_dcc
from lower_graph import detailed_graph, make_graph

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app.title = "Covid India Tracker"

top_row = dbc.Container([
    dbc.Row([cards, india_graph]),
])

second_row = dbc.Container([
    dbc.Row([state_dcc, district_dcc], justify='center'),
    dbc.Row([detailed_graph])
])

app.layout = html.Div(#style={'backgroundColor': 'black'},
    children=[
        new_navbar,
        html.Br(),
        # cards,
        top_row,
        html.Br(),
        dbc.Row(html.H3(children = "State & District Status"), justify = "center"),
        html.Br(),
        second_row,
    ])

# @app.callback(
#     Output("registeration-toast", "is_open"),
#     [Input("sign-up-button", "n_clicks")],
# )
# def open_toast(n):
#     if n:
#         return True
#     return False


@app.callback(
    Output("district-selected-dcc", "options"),
    [Input("state-selected-dcc", "value")]
)
def update_district(state_name):
    return [{'label':district_name, 'value':district_name} for district_name in get_state_to_district_mapping(state_name)]

@app.callback(
    Output("district-selected-nav", "options"),
    [Input("state-selected-nav", "value")]
)
def update_district_nav(state_name_nav):
    return [{'label':district_name, 'value':district_name} for district_name in get_state_to_district_mapping(state_name_nav)]




@app.callback(
    Output("lower_graph", "figure"),
    [Input("state-selected-dcc", "value"),
    Input("district-selected-dcc", "value")]
)
def update_graph2(*args):
    triggered_name = dash.callback_context.triggered[0]['prop_id'].split('.')[0]
    # print(triggered_name)
    triggered_value = dash.callback_context.triggered[0]['value']
    # print(triggered_value)
    if not dash.callback_context.triggered:
        df = state_data_daily("Delhi")
        return make_graph(df, "Delhi")
    if triggered_name == 'state-selected-dcc':
        # print("here\n")
        df = state_data_daily(triggered_value)
        return make_graph(df, triggered_value)
    else:
        df = district_data_daily(triggered_value)
        # print("donee")
        # print(len(df))
        return make_graph(df, triggered_value)



if __name__ == '__main__':
    app.run_server(dev_tools_hot_reload=True, debug=True)
