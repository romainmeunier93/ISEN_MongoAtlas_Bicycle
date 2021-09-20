import requests
import json

def mapNames(station):
    return {"Name": station['fields']['name'], "Coordinates": station['fields']['coordonnees_geo'], "Size": station['fields']['capacity'], "Available": station['fields']['is_renting'], "City": 'Paris', "Municipality": station['fields']['nom_arrondissement_communes']}

def get_velo():
    url = "https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&q=&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes"

    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf-8'))
    response = response_json.get("records", [])

    return list(map(mapNames, response))