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
    district_data.drop_duplicates(subset=['Date'], keep='last', inplace=True)
    return district_data

def state_data_daily(state_name):
    state_data = pd.read_csv('https://api.covid19india.org/csv/latest/states.csv')
    state_data = state_data[['Date', 'State', 'Confirmed','Recovered','Deceased','Other']]
    state_data['Active'] = state_data['Confirmed'] - state_data['Recovered'] - state_data['Deceased'] - state_data['Other']
    state_data.drop_duplicates(keep='first',inplace=True)
    state_data = state_data[state_data['State']==state_name]
    state_data.drop_duplicates(subset=['Date'], keep='last', inplace=True)
    return state_data

def get_state_percent_contribution(state_name):
    india_stats = pd.read_csv("https://api.covid19india.org/csv/latest/case_time_series.csv")
    india_stats = india_stats[-1:]
    india_stats['Active'] = india_stats['Total Confirmed'] - india_stats['Total Recovered'] - india_stats['Total Deceased']

    state_stats = pd.read_csv('https://api.covid19india.org/csv/latest/states.csv')
    state_stats = state_stats[state_stats['State']==state_name]
    state_stats = state_stats[-1:]
    state_stats['Active'] = state_stats['Confirmed'] - state_stats['Recovered'] - state_stats['Deceased'] - state_stats['Other']

    percent_df = pd.DataFrame()
    percent_df['Active'] = 100* list(state_stats['Active'])/india_stats['Active']
    percent_df['Confirmed'] = 100* list(state_stats['Confirmed'])/india_stats['Total Confirmed']
    percent_df['Recovered'] = 100* list(state_stats['Recovered'])/india_stats['Total Recovered']
    percent_df['Deceased'] = 100* list(state_stats['Deceased'])/india_stats['Total deceased']

    return percent_df
