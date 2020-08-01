import dash
import flask
import dash_bootstrap_components as dbc
# import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import os

from get_data import get_state_to_district_mapping, state_data_daily, district_data_daily
from navbar import new_navbar
from total_stats import cards, cards_lower, get_card_layout
from make_graph import make_graph, lower_graph, total_graph
from select_graph_att import state, district

app = dash.Dash(__name__, assets_folder=os.path.dirname(os.path.dirname(__file__)) + "/"+"/assets", external_stylesheets=[dbc.themes.DARKLY, {
    'href': 'https://use.fontawesome.com/releases/v5.8.1/css/all.css',
    'rel': 'stylesheet',
    'integrity': 'sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf',
    'crossorigin': 'anonymous'
}])
server = app.server

app.title = "COVID-19 India Stats Tracker"

# app.head = [
#     html.Link(
#         href="/assets/favicon.ico",
#         rel='icon'
#     ),
# ]


top_row = dbc.Container([
    dbc.Row([cards, dbc.Col(html.Div(), width=0.5), total_graph]),
    # dbc.Row([html.Div()], style=dict(height=10))
])

second_row = dbc.Container([
    dbc.Row(html.H3(children = "State & District Status"), justify = "center"),
    dbc.Row(html.Br()),
    dbc.Row([state, district], justify='center'),
    dbc.Row([cards_lower, dbc.Col(html.Div(), width=0.5), lower_graph])
])

app.layout = html.Div(
    children=[
        dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=app.get_asset_url("logo.png"), height="30px")),
                    # dbc.Col(dbc.NavbarBrand("Navbar", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            # href="https://plot.ly",
        ),

        dbc.NavbarBrand("Covid India Tracker", className="ml-2"),
        # dbc.Collapse(email_bar, id="navbar-collapse", navbar=True)
    ],
    color="dark",
    dark=True,
),
        html.Br(),
        top_row,
        html.Br(),
        second_row,
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Row([dbc.Button(
                html.Span(["", html.I(className="fab fa-github")]), style=dict(marginLeft="5px"), href="https://github.com/sajal-1999/Covid-India-Tracker", target="_blank"),
            dbc.Button(
                html.Span(["", html.I(className="fa fa-envelope")]), style=dict(marginLeft="8px"), href="mailto:covid19indiastats@gmail.com", target="_blank"),
            dbc.Button(
                html.Span(["", html.I(className="fa fa-database")]), style=dict(marginLeft="8px"), href="https://api.covid19india.org/", target="_blank")
        ], justify="center")
    ])

# @app.callback(
#     Output("registeration-toast", "is_open"),
#     [Input("sign-up-button", "n_clicks")],
# )
# def open_toast(n):
#     if n:
#         return True
#     return False

# @server.route('/favicon.ico')
# def favicon():
#     return flask.send_from_directory(os.path.join(server.root_path, 'assets'),
#                                'favicon.ico')



@app.callback(
    Output("district-selected", "options"),
    [Input("state-selected", "value")]
)
def update_district(state_name):
    return [{'label':district_name, 'value':district_name} for district_name in get_state_to_district_mapping(state_name)]

# @app.callback(
#     Output("district-selected-nav", "options"),
#     [Input("state-selected-nav", "value")]
# )
# def update_district_nav(state_name_nav):
#     return [{'label':district_name, 'value':district_name} for district_name in get_state_to_district_mapping(state_name_nav)]

@app.callback(
    [Output("lower_graph", "figure"),
    Output("lower_card", "children")],
    [Input("state-selected", "value"),
    Input("district-selected", "value")]
)
def update_graph(*args):
    triggered_name = dash.callback_context.triggered[0]['prop_id'].split('.')[0]
    triggered_value = dash.callback_context.triggered[0]['value']
    if not dash.callback_context.triggered:
        triggered_name = 'state-selected'
        triggered_value = "Delhi"

    if triggered_name == 'state-selected':
        df = state_data_daily(triggered_value)
        return make_graph(df, triggered_value), dbc.Col(get_card_layout(df[-1:]), align="center")
    else:
        df = district_data_daily(triggered_value)
        return make_graph(df, triggered_value), dbc.Col(get_card_layout(df[-1:]), align="center")


if __name__ == '__main__':
    app.run_server(dev_tools_hot_reload=True, debug=True)
