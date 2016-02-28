

import requests
import json


def getJsonFromWho(linkIn):
    res = requests.get(linkIn) #hardcoded the link in
    if res.status_code == requests.codes.ok:
        return res.text.lower() #really crappy error handling for something that could go so incredibly wrong. srry.
    else:
        print("unable to connect to " + linkIn + " , please check your connection")

def getAPIVariables():
    """
    #auto-generated by pycharm. IDK.
    :rtype: object
    """
    wholeDataset = json.loads(getJsonFromWho("http://apps.who.int/gho/athena/api/GHO.json"))
    apiVariableDict = {}
    assert isinstance(wholeDataset, object) #pycharm told me to put this in, idk why tho.
    for variableObject in wholeDataset['dimension'][0]['code']: #API has this weird thing called a dimension. idk, there's only 1
        #  of them, so it's sorta pointless. All variables and their labels are stored inside an array called 'code'
        #in objects containing a 'label' (variable name you need to call to the API), a 'display' (tells you what it
        #actually does), and a few other things that I'm not really concerned with right now.
        apiVariableDict[variableObject['display']] = variableObject['label']
    return apiVariableDict



def getCountryLabels(): #turning out to be similar to getVariables
    wholeDataset =  json.loads(getJsonFromWho("http://apps.who.int/gho/athena/data/COUNTRY.json"))
    apiVariableDict = {}
    assert isinstance(wholeDataset, object) #pycharm told me to put this in, idk why tho.
    for countryObject in wholeDataset['dimension'][0]['code']:
        apiVariableDict[countryObject['display']] = countryObject['label']
    return apiVariableDict
