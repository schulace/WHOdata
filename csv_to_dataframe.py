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
    return unsorted_data


def sort_by_country(arr_in):
    notDone = True
    while notDone:
        notDone = False
        for x in range(len(arr_in)-1):
            if not alphabetized(arr_in[x][0], arr_in[x+1][0], 0):
                arr_in[x], arr_in[x+1] = arr_in[x+1], arr_in[x]
                notDone = True
    return arr_in


def alphabetized(str1, str2, space_number):
    print(str1 + ", " + str2)
    if str == str2:
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
