import fetcher.variableFetcher
import interpreter.responseSpecifier
import csv_to_dataframe


def get_api_var():
    variable_dictionary = fetcher.variableFetcher.getAPIVariables()
    print("type in what you want information on. (ex. mortality, tobacco, infant, or something more specific)")
    answers = interpreter.responseSpecifier.getMatches(input(), variable_dictionary, True)
    print(answers)
    return answers


def get_country_abbreviation():
    country_dictionary = fetcher.variableFetcher.getCountryLabels()
    print("type in the country you want data for")
    answers = interpreter.responseSpecifier.getMatches(input(), country_dictionary, True)
    print(answers)
    return answers


# print('http://apps.who.int/gho/athena/api/GHO/' + str(getAPIvar()) + ".csv")


