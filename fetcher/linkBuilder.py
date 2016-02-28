def createLink(APIvariable, countryAbrev):
    return 'http://apps.who.int/gho/athena/api/GHO/' + str(APIvariable) + ".csv?filter=COUNTRY:" + str(countryAbrev)
