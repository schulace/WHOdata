import fetcher.variableFetcher
import interpreter.responseSpecifier

def getAPIvar():
    varDict = fetcher.variableFetcher.getAPIVariables() #grabs a dictionary of descriptions as keys, and API variables as values
    print("type in what you want information on. (ex. mortality, tobacco, infant, or something more specific)")
    answers = interpreter.responseSpecifier.getMatches(input(), varDict, True)
    print(answers)
    return answers

def getCountryAbrev():
    countryDict = fetcher.variableFetcher.getCountryLabels()
    print("type in the country you want data for")
    answers = interpreter.responseSpecifier.getMatches(input(), countryDict, True)
    print(answers)
    return answers

print(fetcher.variableFetcher.get_real_variable_names())