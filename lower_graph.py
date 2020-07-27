import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.graph_objs as go
# from get_data import get_data

# callback ---
# fig.add_trace(go.Scatter())
# fig.update_traces(marker=dict(color="RoyalBlue"),
                #   selector=dict(type="bar"))
# 


fig = go.Figure(
    layout = go.Layout(
        legend = dict(font=dict(color="#FFFFFF")),
        # title = 'India overall cases',
        xaxis = dict(title = 'Date', 
                    color="#e8eaed", 
                    dtick=10,
                    gridcolor='#5e5d5e',
                    tickfont=dict(color = "#e8eaed")),
        yaxis = dict(title = 'Cases',
                    color="#e8eaed",
                    # nticks=10,
                    gridcolor='#5e5d5e',
                    tickfont=dict(color = "#e8eaed")),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        dragmode=False,
        hovermode="x",
        # hoverlabel=dict(bgcolor="#4d4e50"),
        titlefont=dict(color='#FFFFFF')
    )
)


lower_graph = dcc.Graph(
    id='lower_graph',
    config={
        "displayModeBar": False, 
        "showTips": False
    }
)

detailed_graph = dbc.Col([lower_graph])