# import dash_bootstrap_components as dbc
import dash_core_components as dcc
# import plotly.graph_objs as go
from get_data import state_data_daily, get_data
from make_graph import make_graph

lower_graph = dcc.Graph(
    id='lower_graph',
    figure=make_graph(state_data_daily("Delhi"), "Delhi"),
    config={
        "displayModeBar": False, 
        "showTips": False
    }
)

total_graph = dcc.Graph(
    id='total_graph', 
    figure = make_graph(get_data(), "India"),
    config={
        "displayModeBar": False, 
        "showTips": False
    }
)