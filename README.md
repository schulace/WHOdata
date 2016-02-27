# WHOdata
python for going through the WHO data via their API.

here's the gist of how this whole thing works.
the fetcher package is used to get a current list of API variables.
    this is accomplished by grabbing a .json file with a lot of meaningless data and sifting through to the 'label' and
    'display' tags.
    these are then passed into a dictionary, with 'display' (the human readable descriptor) as the key and 'display' as
    the value.

after fetching the data, test.py stores it in a variable called varDict.

this is then passed to a function which takes user input and recursively narrows down the dictionary until only 1 pair
matches. Try it out, it'll explain itself better than I just did.
    once it's whittled down to just 1 possibility, it returns the API variable key for that specific descriptor.
*not written yet* the api key is then tacked on to the end of a url as such:
http://apps.who.int/gho/athena/api/GHO/API_KEY_GOES_HERE
from here, a .csv exension can be added to return a csv file, and/ or you can use a ? to specifiy filters, such as
country (by a 3-letter code), year(4-digit integer), and sex (FMLE, MLE, BTSX).

example input output interraction: (user input is in brackets)

type in what you want information on. (ex. mortality, tobacco, infant, or something more specific
user: 'infant'
multiple variable objects match your query. please select from the following:
1) Infant mortality;
2) Number of infant deaths (thousands);
3) Infant mortality rate (probability of dying between birth and age 1 per 1000 live births);
4) Infant mortality rate (per 1000 live births);
5) Infant mortality per 1 000 live births;
6) Infants exclusively breastfed for the first six months of life (%);

user: '5'
EQ_INFANTMORT
