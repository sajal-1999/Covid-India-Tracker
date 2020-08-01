import dash_bootstrap_components as dbc
import dash_html_components as html
from get_data import get_data, state_data_daily

def make_card(df, card_name, color):
    return dbc.Card(
        dbc.CardBody([
            html.H5(card_name, className="text-"+color),
            html.P(df[card_name], className="text-"+color)
        ]),
        color=color,
        outline = True,
        style = {"height": "6rem", "width": "140px"}
    )

def get_card_layout(df):
    return [
        dbc.Row([make_card(df, "Confirmed", "info"), dbc.Col([make_card(df, "Active", "danger")], style=dict(marginLeft="10px"))],
            justify="center",
            no_gutters=False), 
        html.Br(),
        dbc.Row([make_card(df, "Recovered", "success"), dbc.Col([make_card(df, "Deceased", "light")], style=dict(marginLeft="10px"))],
            justify="center",
            no_gutters=False),
        html.Br()
    ]

cards = dbc.Col(get_card_layout(get_data()[-1:]),  align="center")

cards_lower = dbc.Col(get_card_layout(state_data_daily("Delhi")[-1:]), id = "lower_card",  align="center")

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
