import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.graph_objs as go
from get_data import state_data_daily

# callback ---
# fig.add_trace(go.Scatter())
# fig.update_traces(marker=dict(color="RoyalBlue"),
                #   selector=dict(type="bar"))
# 

def make_graph():
    fig = go.Figure(
        layout = go.Layout(
            legend = dict(font=dict(color="#FFFFFF")),
            # title = 'India overall cases',
            xaxis = dict(title = 'Date', 
                        color="#e8eaed", 
                        # dtick=10,
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

    df = state_data_daily("Delhi")
    fig.add_trace(go.Scatter(
        x=df['Date'], 
        y=df['Confirmed'], 
        name='Total Confirmed', 
        hovertemplate = 'Confirmed: %{y}<extra></extra>',
        line=dict(color='#3498DB')
    ))
    fig.add_trace(go.Scatter(
        x=df['Date'], 
        y=df['Active'], 
        name='Total Active', 
        hovertemplate = 'Active: %{y}<extra></extra>',
        line=dict(color='#E74C3C')
    ))
    fig.add_trace(go.Scatter(
        x=df['Date'], 
        y=df['Recovered'],  
        name='Total Recovered',
        hovertemplate = 'Recovered: %{y}<extra></extra>',
        line=dict(color='#00bc8c')
    ))
    fig.add_trace(go.Scatter(
        x=df['Date'], 
        y=df['Deceased'], 
        name='Total Deceased',
        hovertemplate = 'Deceased: %{y}<extra></extra>',
        line=dict(color='#adb5bd')
    ))
    return fig

lower_graph = dcc.Graph(
    id='lower_graph',
    figure=make_graph(),
    config={
        "displayModeBar": False, 
        "showTips": False
    }
)

detailed_graph = dbc.Col([lower_graph])