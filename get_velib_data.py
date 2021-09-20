import requests
import json

def get_velib():
    url = "https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&q=&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes"

    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf-8'))
    return response_json.get("records", [])

print(get_velib())