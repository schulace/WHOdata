import csv
from pandas import DataFrame
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
        try:
            unsorted_data.append([data_arr[x][country_loc],  int(data_arr[x][year_loc]), float(data_arr[x][value_loc])])
        except:
           4 ==4  # pycharm: statement seems to have no effect. me: that's the idea.
    return unsorted_data


def sort_by_country(arr_in):
    sort = False
    while not sort:
        sort = True
        for x in range(len(arr_in)-1):
            if not alphabetized(arr_in[x][0].strip(), arr_in[x+1][0].strip(), 0):
                temp1 = arr_in[x]
                temp2 = arr_in[x + 1]
                arr_in[x] = temp2
                arr_in[x+1] = temp1
                sort = False
    return arr_in


def alphabetized(str1, str2, space_number):
    if str1 == str2:
        return True
    elif space_number > len(str1) and space_number < len(str2):
        return False
    elif space_number > len(str2) and space_number < len(str1):
        return True
    else:
        if ord(str1[space_number]) < ord(str2[space_number]):
            return True
        elif ord(str1[space_number]) > ord(str2[space_number]):
            return False
        else:
            return alphabetized(str1, str2, space_number + 1)


def make_panda_data(arr_in):
    df = pd.DataFrame(arr_in).sort_index()
    return df
