import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.graph_objs as go
from get_data import get_data

# fig = px.line(get_data(), x = 'Date', y=['Total Confirmed', 'Total Recovered', 'Total Deceased'])
fig = go.Figure()
fig.add_trace(go.Scatter(x=get_data()['Date'], y=get_data()['Total Confirmed'], name='Total Cofirmed', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=get_data()['Date'], y=get_data()['Total Deceased'], name='Total Deceased', line=dict(color='red', dash='dot')))
fig.add_trace(go.Scatter(x=get_data()['Date'], y=get_data()['Total Recovered'], name='Total Recovered', line=dict(color='green')))
fig.add_trace(go.Scatter(x=get_data()['Date'], y=get_data()['Active'], name='Total Active', line=dict(color='yellow')))
# fig.add_trace(go.Scatter(x=get_data()['Date'], y=get_data()['Total Confirmed'], line=dict(color='blue')))

fig.update_layout(
    xaxis_title = 'Date',
    yaxis_title = 'Cases',
    title = 'India overall cases'
#     plot_bgcolor="black"
)

total_graph = dcc.Graph(id='total_graph', figure = fig)

india_graph = dbc.Col([total_graph])