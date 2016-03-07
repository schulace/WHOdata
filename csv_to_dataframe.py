import csv
#  import pandas as pd
import operator


def get_csv_array(file_location):
    fileIn = open(file_location)
    reader = csv.reader(fileIn)
    data_arr = list(reader)
    year_loc = operator.indexOf('YEAR',data_arr[0])
    country_loc = operator.indexOf('COUNTRY', data_arr[0])
    value_loc = operator.indexOf('Numeric', data_arr[0])
    unsorted_data = []
    for x in range(1, len(data_arr)):
        unsorted_data[x-1] = [data_arr[x][country_loc], data_arr[x][year_loc], data_arr[x][value_loc]]
