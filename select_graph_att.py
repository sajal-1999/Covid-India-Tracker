from get_data import get_state_list
import dash_core_components as dcc

state = dcc.Dropdown(
        id="state-selected",
        value='Delhi',
        clearable=False,
        style=dict(width = '250px', color="black", verticalAlign="right"),
        options=[{'label':state_name, 'value':state_name} for state_name in get_state_list()]
    )

district = dcc.Dropdown(
        id="district-selected",
        clearable=False,
        style=dict(width = '250px', color="black", marginLeft="5px", verticalAlign="middle"),
        # options=[{'label':district_name, 'value':district_name} for district_name in get_state_to_district_mapping(state_name)]
    )