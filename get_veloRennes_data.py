import requests
import json

def get_veloRennes():
    url = "https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=etat-des-stations-le-velo-star-en-temps-reel&q=&facet=nom&facet=etat&facet=nombreemplacementsactuels&facet=nombreemplacementsdisponibles&facet=nombrevelosdisponibles"

    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf-8'))
    return response_json.get("records", [])

print(get_veloRennes())


