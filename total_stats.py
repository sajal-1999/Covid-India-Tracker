import dash_bootstrap_components as dbc
import dash_html_components as html
from get_data import get_data, state_data_daily

df = get_data()[-1:]

def make_card(df, card_name, color):
    return dbc.Card(
        dbc.CardBody([
            html.H4(card_name, className="text-"+color),
            html.P(df[card_name], className="text-"+color)
        ]),
        color=color,
        outline = True,
        style = {"height": "6rem", "width": "10rem"}
    )

cards = dbc.Col([
    dbc.Row([make_card(df, "Confirmed", "info")],
        justify="center",
        no_gutters=False), html.Br(),
    dbc.Row([make_card(df, "Active", "danger")],
        justify="center",
        no_gutters=False), html.Br(),
    dbc.Row([make_card(df, "Recovered", "success")],
        justify="center",
        no_gutters=False), html.Br(),
    dbc.Row([make_card(df, "Deceased", "light")],
        justify="center",
        no_gutters=False)
    ], width={"size": 1.25}, align="center")

df_1 = state_data_daily("Delhi")[-1:]
cards_lower = dbc.Col([
    dbc.Col([dbc.Row([make_card(df_1, "Confirmed", "info")], 
        justify="center", 
        no_gutters=False), html.Br(), 
    dbc.Row([make_card(df_1, "Active", "danger")], 
        justify="center", 
        no_gutters=False)]),
    dbc.Col([dbc.Row([make_card(df_1, "Recovered", "success")], 
        justify="center", 
        no_gutters=False), html.Br(), 
    dbc.Row([make_card(df_1, "Deceased", "light")], 
        justify="center", 
        no_gutters=False)])
    ], width={"size": 1.25}, align="center", id="lower_card")

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
