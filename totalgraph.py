import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.graph_objs as go
from get_data import get_data
from lower_graph import make_graph

# def get_graph_data(df, att, color_code):
#     return go.Scatter(
#         x=df['Date'], 
#         y=df['Total ' + att], 
#         name='Total' + att, 
#         connectgaps = True,
#         hovertemplate = att + ': %{y}<extra></extra>',
#         line=dict(color=color_code))

# confirmed = go.Scatter(
#     x=get_data()['Date'], 
#     y=get_data()['Total Confirmed'], 
#     name='Total Confirmed', 
#     hovertemplate = 'Confirmed: %{y}<extra></extra>',
#     line=dict(color='#3498DB')
# )
# active = go.Scatter(
#     x=get_data()['Date'], 
#     y=get_data()['Total Active'], 
#     name='Total Active', 
#     hovertemplate = 'Active: %{y}<extra></extra>',
#     line=dict(color='#E74C3C')
# )
# recovered = go.Scatter(
#     x=get_data()['Date'], 
#     y=get_data()['Total Recovered'], 
#     name='Total Recovered',
#     hovertemplate = 'Recovered: %{y}<extra></extra>',
#     line=dict(color='#00bc8c')
# )
# deceased = go.Scatter(
#     x=get_data()['Date'], 
#     y=get_data()['Total Deceased'], 
#     name='Total Deceased',
#     hovertemplate = 'Deceased: %{y}<extra></extra>',
#     line=dict(color='#adb5bd')
# )

# fig = go.Figure(
#     data = [confirmed, active, recovered, deceased],
#     layout = go.Layout(
#         legend = dict(font=dict(color="#FFFFFF")),
#         title = 'India overall cases',
#         xaxis = dict(title = 'Date', 
#                     color="#e8eaed", 
#                     dtick=10,
#                     gridcolor='#5e5d5e',
#                     tickfont=dict(family="Times New Roman", color = "#e8eaed")),
#         yaxis = dict(title = 'Cases',
#                     color="#e8eaed",
#                     # nticks=10,
#                     gridcolor='#5e5d5e',
#                     zeroline=True,
#                     zerolinecolor='white',
#                     tickfont=dict(family="Times New Roman", color = "#e8eaed")),
#         paper_bgcolor='rgba(0,0,0,0)',
#         plot_bgcolor='rgba(0,0,0,0)',
#         dragmode=False,
#         hovermode="x",
#         # hoverlabel=dict(bgcolor="#4d4e50"),
#         titlefont=dict(color='#FFFFFF')
#     )
# )


total_graph = dcc.Graph(
    id='total_graph', 
    figure = make_graph(get_data(), "India"),
    config={
        "displayModeBar": False, 
        "showTips": False
    }
)

india_graph = dbc.Col([total_graph])