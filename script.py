import json
import requests

def function():
    url = "http://app.objco.com:8099/?account=1IF0PIBK37&limit=5"
    # Get dummy data using an API
    reponse = requests.get(url)
    print(reponse)

    # Convert data to dict
    data = json.loads(reponse.text)

    # Convert dict to string
    data = json.dumps(data)

    print(data)
    print(type(data))
    return data

function()
