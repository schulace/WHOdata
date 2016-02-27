def getMatches(userInput, varList, firstTime):
    possibleMatches = {}
    possibleMatchkeys = []
    for key in varList:
        if userInput.lower() in key.lower():
            if userInput.lower() == key.lower() and not firstTime:
                return varList[key]
            possibleMatches[key] = varList[key]
            possibleMatchkeys.append(key)
    if len(possibleMatches) == 0:
        print("couldn't find any API variables matching your description")
    elif len(possibleMatches) == 1:
        return possibleMatches[userInput]
    else:
        return getMatches(pickerDialogue(possibleMatchkeys), possibleMatches, False)


def pickerDialogue(keyArrIn):
    print("multiple variable objects match your query. please select from the following:")
    x = 1;
    for key in keyArrIn:
        print(str(x) + ") " + key, end=";\n")
        x += 1
    print()
    userResponse = getInteger(input(), x)
    return keyArrIn[userResponse -1]

def getInteger(userIn, upper):
    try:
        integer =  int(userIn)
    except ValueError:
        print("not an integer")
        return getInteger(input(), upper)
    if upper >= integer >= 1:
        return integer
    else:
        print("the number you specified is not within the required range")
        return getInteger(input(), upper)

