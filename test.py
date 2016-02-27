import fetcher.variableFetcher
import interpreter.responseSpecifier


varDict = fetcher.variableFetcher.getVariables() #grabs a dictionary of descriptions as keys, and API variables as values
print("type in what you want information on. (ex. mortality, tobacco, infant, or something more specific)")
answers = interpreter.responseSpecifier.getMatches(input(), varDict)
print(answers)

