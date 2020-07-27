import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.graph_objs as go
from get_data import get_data

# fig = px.line(get_data(), x = 'Date', y=['Total Confirmed', 'Total Recovered', 'Total Deceased'])
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=get_data()['Date'], y=get_data()['Total Confirmed'], name='Total Cofirmed', line=dict(color='blue')))
# fig.add_trace(go.Scatter(x=get_data()['Date'], y=get_data()['Total Deceased'], name='Total Deceased', line=dict(color='red', dash='dot')))
# fig.add_trace(go.Scatter(x=get_data()['Date'], y=get_data()['Total Recovered'], name='Total Recovered', line=dict(color='green')))
# fig.add_trace(go.Scatter(x=get_data()['Date'], y=get_data()['Active'], name='Total Active', line=dict(color='yellow')))
# fig.add_trace(go.Scatter(x=get_data()['Date'], y=get_data()['Total Confirmed'], line=dict(color='blue')))

confirmed = go.Scatter(x=get_data()['Date'], y=get_data()['Total Confirmed'], name='Total Cofirmed', line=dict(color='#3498DB'))
active = go.Scatter(x=get_data()['Date'], y=get_data()['Active'], name='Total Active', line=dict(color='#F39C12'))
recovered = go.Scatter(x=get_data()['Date'], y=get_data()['Total Recovered'], name='Total Recovered', line=dict(color='#00bc8c'))
deceased = go.Scatter(x=get_data()['Date'], y=get_data()['Total Deceased'], name='Total Deceased', line=dict(color='#E74C3C', dash='dot'))

fig = go.Figure(
        data = [confirmed, active, recovered, deceased],
        layout = go.Layout(
            legend = dict(font=dict(color="#FFFFFF")),
            title = 'India overall cases',
            hovermode="x",
            xaxis = dict(title = 'Date', 
                        color="#e8eaed", 
                        dtick=10,
                        gridcolor='#5e5d5e',
                        tickfont=dict(family="Times New Roman", color = "#e8eaed")),
            yaxis = dict(title = 'Cases',
                        color="#e8eaed",
                        # nticks=10,
                        gridcolor='#5e5d5e',
                        tickfont=dict(family="Times New Roman", color = "#e8eaed")),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            titlefont=dict(color='#FFFFFF'))
        )


total_graph = dcc.Graph(
    id='total_graph', 
    figure = fig,
    config={"displayModeBar": False, "showTips": False}
     )

india_graph = dbc.Col([total_graph])