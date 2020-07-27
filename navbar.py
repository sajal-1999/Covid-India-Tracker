import dash_bootstrap_components as dbc

email_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="email", placeholder="Email")),
        dbc.Col(dbc.Input(type="district", placeholder="District")),
        dbc.Col(
            dbc.Button("Signup for daily updates", color="primary", className="ml-2"),
            width="auto",
        ),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

new_navbar = dbc.Navbar(
    [
        # html.A(
        #     # Use row and col to control vertical alignment of logo / brand
        #     dbc.Row(
        #         [
        #             dbc.Col(html.Img(src="filename.png", height="30px")),
        #             dbc.Col(dbc.NavbarBrand("Navbar", className="ml-2")),
        #         ],
        #         align="center",
        #         no_gutters=True,
        #     ),
        #     href="https://plot.ly",
        # ),

        dbc.NavbarBrand("Covid India Tracker", className="ml-2"),
        dbc.Collapse(email_bar, id="navbar-collapse", navbar=True)
    ],
    color="dark",
    dark=True,
)

navbar = dbc.NavbarSimple(
    # children=[
    #     dbc.NavItem(dbc.NavLink("Covid India Tracker", href="#"))
    # ],
    brand="Covid India Tracker",
    brand_href="#",
    color="dark",
    dark=True,
)