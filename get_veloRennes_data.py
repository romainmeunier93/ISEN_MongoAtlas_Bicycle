import requests
import json

def mapNames(station):
    return {"Name": station['fields']['nom'], "Coordinates": station['fields']['coordonnees'], "Size": station['fields']['nombreemplacementsactuels'], "Available": station['fields']['etat'], "City": 'Rennes'}

def get_velo():
    url = "https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=etat-des-stations-le-velo-star-en-temps-reel&q=&facet=nom&facet=etat&facet=nombreemplacementsactuels&facet=nombreemplacementsdisponibles&facet=nombrevelosdisponibles"

    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf-8'))
    response = response_json.get("records", [])

    return list(map(mapNames, response))
