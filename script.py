import json
import requests
import meteo
from tinydb import TinyDB, Query

def function():
    url = "http://app.objco.com:8099/?account=1IF0PIBK37&limit=5"
    # Get dummy data using an API
    reponse = requests.get(url)

    # loads : create a json object
    data = json.loads(reponse.text)
    list_meteo = meteo.create_meteo_object_from_data(data)
    res = ""
    for x in list_meteo :
        res += meteo.toString(x) + "\n"
    print(res)
    return res

function()
