import dash_bootstrap_components as dbc
import dash_core_components as dcc
from get_data import get_data

df = get_data()
print(df[-1:])


# make a dbc row with cards as columns
# each card denotes 1 latest detail