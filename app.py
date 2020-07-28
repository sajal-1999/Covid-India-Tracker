import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
# # import plotly.express as px

from get_data import *
from totalgraph import india_graph
from navbar import *
from total_stats import cards
from select_graph_att import *
from lower_graph import detailed_graph

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app.title = "Covid India Tracker"

top_row = dbc.Container([
    dbc.Row([cards, india_graph]),
    # dbc.Row([state graph])
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
def update_district(state_name_graph):
    return [{'label':district_name, 'value':district_name} for district_name in get_state_to_district_mapping(state_name_graph)]

@app.callback(
    Output("district-selected-nav", "options"),
    [Input("state-selected-nav", "value")]
)
def update_district_nav(state_name_nav):
    return [{'label':district_name, 'value':district_name} for district_name in get_state_to_district_mapping(state_name_nav)]


# @app.callback(
#     Output("lower_graph", "figure"),
#     [Input("state-selected-dcc", "value")]
# )
# def update_graph2(state_name11):

#     # fig.update_traces(marker=dict(color="RoyalBlue"),
#     #                 selector=dict(name="bar"))
#     # return fig
#     pass





if __name__ == '__main__':
    app.run_server(dev_tools_hot_reload=True, debug=True)
