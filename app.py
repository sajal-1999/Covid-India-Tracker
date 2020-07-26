import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# import plotly.express as px
import plotly.graph_objects as go
import plotly.express as px
from get_data import get_data, get_state_list_options

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# fig = px.line(get_data(), x = 'Date', y=['Total Confirmed', 'Total Recovered', 'Total Deceased'])
fig = go.Figure()
fig.add_trace(go.Scatter(x=get_data()['Date'], y=get_data()['Total Confirmed'], name='Total Cofirmed', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=get_data()['Date'], y=get_data()['Total Deceased'], name='Total Deceased', line=dict(color='red', dash='dot')))
fig.add_trace(go.Scatter(x=get_data()['Date'], y=get_data()['Total Recovered'], name='Total Recovered', line=dict(color='green')))
# fig.add_trace(go.Scatter(x=get_data()['Date'], y=get_data()['Total Confirmed'], line=dict(color='blue')))

fig.update_layout(
    xaxis_title = 'Date',
    yaxis_title = 'Cases',
    title = 'India overall cases'
#     plot_bgcolor="black"
)

app.layout = html.Div(#style={'backgroundColor': 'black'},
    children=[
    html.H1('Hello user', style = {'textAlign': 'center', 'color': 'red'}),
    html.Div(children = '''
        Dash: A web application framework for Python.
    '''),
    dcc.Graph(
        id = 'example-graph',
        figure = fig
    ),
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=get_state_list_options(),
        value='AN'
    )
])

if __name__ == '__main__':
    app.run_server(dev_tools_hot_reload=True, debug=True)
