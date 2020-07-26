import pandas as pd
# import numpy as np

def get_data():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/case_time_series.csv")
    return df

# print(get_data()['Total Deceased'][:10])
# print(get_data().columns)