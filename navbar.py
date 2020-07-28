import dash_bootstrap_components as dbc
import dash_core_components as dcc
from get_data import get_state_list,  get_state_to_district_mapping

state_list_nav = []
for i in get_state_list():
    state_list_nav.append(dbc.DropdownMenuItem(i))

district_list = []
state_name = 'Maharashtra' #Kept static for now. Need to fetch from state drop-down
for i in get_state_to_district_mapping(state_name):
    district_list.append(dbc.DropdownMenuItem(i))
# email_bar = dbc.Row(
#     [
#         dbc.Col(dbc.Input(type="email", placeholder="Email")),
#         dbc.Col(dbc.DropdownMenu(label="Select State", id="state-selected-nav", children=state_list_nav, right=True)),
#         dbc.Col(dbc.DropdownMenu(label="Select District", id="district-selected-nav", children=district_list, right=True)),
#         dbc.Col(
#             dbc.Button("Signup for daily updates", color="primary", className="ml-2", id="sign-up-button"),
#             width="auto",
#         ),
#         dbc.Toast(
#             "Select state and district details to get personalised mails",
#             id = "registeration-toast",
#             header = "Enter all details",
#             dismissable = True,
#             icon="danger",
#             style={'position': "fixed", 'top': 66, 'right': 10, ' width':350}
#         )
#     ],
#     no_gutters=True,
#     className="ml-auto flex-nowrap mt-3 mt-md-0",
#     align="center",
# )

state_dcc_nav = dbc.Col([
    dcc.Dropdown(
        id="state-selected-nav",
        value='Delhi',
        style=dict(width = '250px', color="black"),
        options=[{'label':state_name, 'value':state_name} for state_name in get_state_list()]
    )])

district_dcc_nav = dbc.Col([
    dcc.Dropdown(
        id="district-selected-nav",
        # className = "mb-3",
        style=dict(width = '250px', color="black"),
        # options=[{'label':district_name, 'value':district_name} for district_name in get_state_to_district_mapping(state_name)]
    )])

email_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="email", placeholder="Email")),
        state_dcc_nav,
        district_dcc_nav,
        dbc.Col(
            dbc.Button("Signup for daily updates", color="primary", className="ml-2", id="sign-up-button"),
            width="auto",
        ),
        dbc.Toast(
            "Select state and district details to get personalised mails",
            id = "registeration-toast",
            header = "Enter all details",
            dismissable = True,
            icon="danger",
            style={'position': "fixed", 'top': 66, 'right': 10, ' width':350}
        )
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
