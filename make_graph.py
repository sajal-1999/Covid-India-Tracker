import dash_core_components as dcc
import plotly.graph_objs as go
from get_data import state_data_daily, get_data

def get_graph_data(df, att, color_code):
    return go.Scatter(
        x=df['Date'],
        y=df[att],
        name='Total ' + att,
        connectgaps = True,
        hovertemplate = att + ': %{y}<extra></extra>',
        line=dict(color=color_code))

def make_graph(df, region):
    fig = go.Figure(
        data = [
            get_graph_data(df, 'Confirmed', '#3498DB'),
            get_graph_data(df, 'Active', '#E74C3C'),
            get_graph_data(df, 'Recovered', '#00bc8c'),
            get_graph_data(df, 'Deceased', '#adb5bd'),
        ],
        layout = go.Layout(
            legend = dict(font=dict(color="#FFFFFF")),
            title = region + ' Cumulative Cases',
            xaxis = dict(title = dict(text='Date', font=dict(size=20)),
                        color="#e8eaed",
                        gridcolor='#5e5d5e',
                        tickfont=dict(color = "#e8eaed")),
            yaxis = dict(title = dict(text='Cases', font=dict(size=20)),
                        color="#e8eaed",
                        gridcolor='#5e5d5e',
                        tickfont=dict(color = "#e8eaed")),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            dragmode=False,
            hovermode="x",
            height = 500,
            width = 800,
            titlefont=dict(color='#FFFFFF')
        )
    )
    return fig

def get_graph():
    pass

lower_graph = dcc.Graph(
    id='lower_graph',
    figure=make_graph(state_data_daily("Delhi"), "Delhi"),
    config={
        "displayModeBar": False,
        "showTips": False
    }
)

df = get_data()
total_graph = dcc.Graph(
    id='total_graph',
    # figure = make_graph(get_data(), "India"),
    figure = go.Figure(
        data = [
            get_graph_data(df, 'Confirmed', '#3498DB'),
            get_graph_data(df, 'Active', '#E74C3C'),
            get_graph_data(df, 'Recovered', '#00bc8c'),
            get_graph_data(df, 'Deceased', '#adb5bd'),
        ],
        layout = go.Layout(
            legend = dict(font=dict(color="#FFFFFF")),
            title = "India Overall Cases",
            xaxis = dict(title = dict(text='Date', font=dict(size=20)),
                        color="#e8eaed",
                        dtick=15,
                        gridcolor='#5e5d5e',
                        tickfont=dict(color = "#e8eaed")),
            yaxis = dict(title = dict(text='Cases', font=dict(size=20)),
                        color="#e8eaed",
                        nticks=5,
                        gridcolor='#5e5d5e',
                        tickfont=dict(color = "#e8eaed")),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            dragmode=False,
            hovermode="x",
            height = 500,
            width = 800,
            titlefont=dict(color='#FFFFFF')
        )
    ),
    config={
        "displayModeBar": False,
        "showTips": False
    }
)
