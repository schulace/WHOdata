import csv
from pandas import DataFrame
import pandas as pd
import operator


def get_csv_array(file_location):
    fileIn = open(file_location)
    reader = csv.reader(fileIn)
    data_arr = list(reader)
    print(data_arr)
    first_line = data_arr[0]
    year_loc = data_arr[0].index('YEAR')
    country_loc = data_arr[0].index('COUNTRY')
    value_loc = data_arr[0].index('Numeric')
    unsorted_data = []
    print(data_arr[0][value_loc])
    for x in range(1, len(data_arr)):
        try:
            unsorted_data.append({'Country':data_arr[x][country_loc], 'Year': int(data_arr[x][year_loc]), 'value': float(data_arr[x][value_loc])})
        except:
            print('no data for this nation / year, not putting into DataFrame')
    print(unsorted_data)
    return unsorted_data


def make_panda_data(arr_in):
    df = pd.DataFrame(arr_in).sort_index()
    return df
