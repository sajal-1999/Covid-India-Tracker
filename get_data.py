import pandas as pd
# import numpy as np

def get_data():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/case_time_series.csv")
    df['Active'] = df['Total Confirmed'] - df['Total Recovered'] - df['Total Deceased']
    return df[-100:]

def get_state_list_options():
    district_wise = pd.read_csv('https://api.covid19india.org/csv/latest/district_wise.csv')
    # return district_wise['State'].unique()
    state_to_code_map = pd.DataFrame()
    state_to_code_map['label'] = district_wise['State']
    state_to_code_map['value'] = district_wise['State_Code']
    state_to_code_map.drop_duplicates(keep='first', inplace=True)
    state_to_code_map.drop([0], inplace = True)
    state_list_options = state_to_code_map.to_dict(orient='records')
    return state_list_options

def get_state_list():
    district_wise = pd.read_csv('https://api.covid19india.org/csv/latest/district_wise.csv')
    district_wise.drop([0], inplace = True)
    return district_wise['State'].unique()

def get_state_to_district_mapping(state_name):
    district_mapping = pd.read_csv('https://api.covid19india.org/csv/latest/district_wise.csv')
    district_mapping = district_mapping[['State_Code', 'State','District_Key', 'District']]
    district_mapping.drop_duplicates(keep='first',inplace=True)
    district_mapping = district_mapping[district_mapping['State']==state_name]
    district_mapping = district_mapping[district_mapping['District']!='Other State']
    return district_mapping
