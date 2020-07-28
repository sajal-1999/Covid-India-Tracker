from get_data import get_state_list, get_state_to_district_mapping
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


state_list = []
for i in get_state_list():
    state_list.append(dbc.DropdownMenuItem(i, id=i))

district_list = []
state_name = 'Maharashtra' #Kept static for now. Need to fetch from state drop-down
for i in get_state_to_district_mapping(state_name):
    district_list.append(dbc.DropdownMenuItem(i, id= i))


state = dbc.InputGroup([
    dbc.DropdownMenu(
        label="Select State",
        id="state-selected",
        children=state_list,
        className="mb-3",
        right=True
)])

district = dbc.InputGroup([
    dbc.DropdownMenu(
        label="Select District",
        id="district-selected",
        children=district_list,
        className="mb-3",
        right=True
)])


state_dcc = dbc.Col([
    dcc.Dropdown(
        id="state-selected-dcc",
        value='Delhi',
        style=dict(width = '250px', color="black"),
        options=[{'label':state_name, 'value':state_name} for state_name in get_state_list()]
    )])

district_dcc = dbc.Col([
    dcc.Dropdown(
        id="district-selected-dcc",
        # className = "mb-3",
        style=dict(width = '250px', color="black"),
        # options=[{'label':district_name, 'value':district_name} for district_name in get_state_to_district_mapping(state_name)]
    )])
