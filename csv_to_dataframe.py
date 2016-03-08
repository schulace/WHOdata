import csv
import pandas as pd
import operator


def get_csv_array(file_location):
    fileIn = open(file_location)
    reader = csv.reader(fileIn)
    data_arr = list(reader)
    first_line = data_arr[0]
    year_loc = data_arr[0].index('YEAR')
    country_loc = data_arr[0].index('COUNTRY')
    value_loc = data_arr[0].index('Numeric')
    unsorted_data = []

    for x in range(1, len(data_arr)):
        unsorted_data.append([data_arr[x][country_loc], data_arr[x][year_loc], data_arr[x][value_loc]])
    print(unsorted_data)
