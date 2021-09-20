import requests
import json

def mapNames(station):
    return {"Name": station['fields']['nom'], "Coordinates": station['fields']['localisation'], "Size": station['fields']['nbvelosdispo'] + station['fields']['nbplacesdispo'], "TPE": station['fields']['type'], "Available": station['fields']['etat'], "City": 'Lille', "Municipality": station['fields']['commune']}

def get_velo():
    url = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&rows=3000&facet=libelle&facet=nom&facet=commune&facet=etat&facet=type&facet=etatconnexion"

    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf-8'))
    response = response_json.get("records", [])

    return list(map(mapNames, response))