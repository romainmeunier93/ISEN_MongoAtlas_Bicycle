import requests
import json

file = open("cities_uris.json", "r")
cities_uris = json.load(file)

def get_velo(city, mapNames):
    url = cities_uris[city]

    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf-8'))

    if city == "Lyon":
        response = response_json
    else:
        response = response_json.get("records", [])

    return list(map(mapNames, response))