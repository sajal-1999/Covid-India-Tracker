import pandas as pd
# import numpy as np

def get_data():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/case_time_series.csv")
    df['Active'] = df['Total Confirmed'] - df['Total Recovered'] - df['Total Deceased']
    df.rename(columns = {'Total Confirmed':'Confirmed'}, inplace = True)
    df.rename(columns = {'Total Recovered':'Recovered'}, inplace = True)
    df.rename(columns = {'Total Deceased':'Deceased'}, inplace = True)
    return df[-100:]

# def get_state_list_options():
#     district_wise = pd.read_csv('https://api.covid19india.org/csv/latest/district_wise.csv')
#     # return district_wise['State'].unique()
#     state_to_code_map = pd.DataFrame()
#     state_to_code_map['label'] = district_wise['State']
#     state_to_code_map['value'] = district_wise['State_Code']
#     state_to_code_map.drop_duplicates(keep='first', inplace=True)
#     state_to_code_map.drop([0], inplace = True)
#     state_list_options = state_to_code_map.to_dict(orient='records')
#     return state_list_options

def get_state_list():
    district_wise = pd.read_csv('https://api.covid19india.org/csv/latest/district_wise.csv')
    district_wise.drop([0], inplace = True)
    return district_wise['State'].unique()

def get_state_to_district_mapping(state_name):
    district_data_unavailable = ['Delhi', 'Andaman and Nicobar Islands', 'Chandigarh', 'Telangana']
    if state_name in district_data_unavailable:
        return []
    district_mapping = pd.read_csv('https://api.covid19india.org/csv/latest/district_wise.csv')
    district_mapping = district_mapping[['State','District']]
    district_mapping.drop_duplicates(keep='first',inplace=True)
    district_mapping = district_mapping[district_mapping['State']==state_name]
    district_mapping = district_mapping[district_mapping['District']!='Other State']
    district_mapping = district_mapping[district_mapping['District']!='Foreign Evacuees']
    district_mapping = district_mapping[district_mapping['District']!='Unknown']
    district_mapping = district_mapping[district_mapping['District']!='Airport Quarantine']
    district_mapping = district_mapping[district_mapping['District']!='Railway Quarantine']
    return list(district_mapping['District'])

def district_data_daily(district_name):
    district_data = pd.read_csv('https://api.covid19india.org/csv/latest/districts.csv')
    district_data = district_data[['Date','District','Confirmed','Recovered','Deceased']]
    district_data['Active'] = district_data['Confirmed'] - district_data['Recovered'] - district_data['Deceased']
    district_data.drop_duplicates(keep='first',inplace=True)
    district_data = district_data[district_data['District']==district_name]
    return district_data

def state_data_daily(state_name):
    state_data = pd.read_csv('https://api.covid19india.org/csv/latest/states.csv')
    state_data = state_data[['Date', 'State', 'Confirmed','Recovered','Deceased','Other']]
    state_data['Active'] = state_data['Confirmed'] - state_data['Recovered'] - state_data['Deceased'] - state_data['Other']
    state_data.drop_duplicates(keep='first',inplace=True)
    state_data = state_data[state_data['State']==state_name]
    return state_data
