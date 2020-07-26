import pandas as pd
# import numpy as np

def get_data():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/case_time_series.csv")
    return df

def get_state_list_options():
    district_wise = pd.read_csv('https://api.covid19india.org/csv/latest/district_wise.csv')
    state_to_code_map = pd.DataFrame()
    state_to_code_map['label'] = district_wise['State']
    state_to_code_map['value'] = district_wise['State_Code']
    state_to_code_map.drop_duplicates(keep='first', inplace=True)
    state_to_code_map.drop([0], inplace = True)
    state_list_options = state_to_code_map.to_dict(orient='records')
    return state_list_options