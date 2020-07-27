import dash_bootstrap_components as dbc
import dash_html_components as html
from get_data import get_data

df = get_data()[-1:]

confirmed = dbc.Card(
    dbc.CardBody([
        html.H4("Confirmed", className="text-info"),
        html.P(df['Total Confirmed'], className="text-info")
    ]),
    color="primary",
    outline = True,
    style = {"height": "6rem", "width": "10rem"}
)

active = dbc.Card(
    dbc.CardBody([
        html.H4("Active", className="text-warning"),
        html.P(df['Active'], className="text-warning")
    ]),
    color="warning",
    outline = True,
    style = {"height": "6rem", "width": "10rem"}
)

recovered = dbc.Card(
    dbc.CardBody([
        html.H4("Recovered", className="text-success"),
        html.P(df['Total Recovered'], className="text-success")
    ]),
    color="success",
    outline = True,
    style = {"height": "6rem", "width": "10rem"}
)

death = dbc.Card(
    dbc.CardBody([
        html.H4("Deaths", className="text-danger"),
        html.P(df['Total Deceased'], className="text-danger")
    ]),
    color="danger",
    outline = True,
    style = {"height": "6rem", "width": "10rem"}
)

cards = dbc.Col([
    dbc.Row([confirmed], justify="center", no_gutters=False), html.Br(), 
    dbc.Row([active], justify="center", no_gutters=False), html.Br(), 
    dbc.Row([recovered], justify="center", no_gutters=False), html.Br(), 
    dbc.Row([death], justify="center", no_gutters=False)
    ], width={"size": 1.5}, align="center")

# carddeck = dbc.CardDeck([confirmed, active, recovered, death], style={"width": "50rem"})

# cards = dbc.Row([
#     carddeck
#     ], justify="center")

# cards = dbc.Row([
#     dbc.Col(confirmed, width={"size": 1.5, "order": 1}),
#     dbc.Col(active, width={"size": 1.5, "order": 2,}), 
#     dbc.Col(recovered, width={"size": 1.5, "order": 3,}),
#     dbc.Col(death, width={"size": 1.5, "order": 4})
# ], justify="center", no_gutters=False)