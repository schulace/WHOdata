

import requests
import json
import fetcher
#json_data=open("http://apps.who.int/gho/athena/api/GHO.json").read()


def getJsonFromWho():
    res = requests.get("http://apps.who.int/gho/athena/api/GHO.json")
    if res.status_code == requests.codes.ok:
        return res.text #really crappy error handling for something that could go so incredibly wrong. srry.
    else:
        print("unable to connect to http://apps.who.int/gho/athena/api/GHO.json, please check your connection")

def getVariables():
    """
    #auto-generated by pycharm. IDK.
    :rtype: object
    """
    jsonAsDict = json.loads(getJsonFromWho())
    newDict = {}
    assert isinstance(jsonAsDict, object) #pycharm told me to put this in, idk why tho.
    for thing in jsonAsDict['dimension'][0]['code']: #API has this weird thing called a dimension. idk, there's only 1
        #  of them, so it's sorta pointless. All variables and their labels are stored inside an array called 'code'
        #in objects containing a 'label' (variable name you need to call to the API), a 'display' (tells you what it
        #actually does), and a few other things that I'm not really concerned with right now.
        newDict[thing['display']] = thing['label']
    return newDict
