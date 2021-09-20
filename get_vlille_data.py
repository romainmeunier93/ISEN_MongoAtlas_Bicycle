import requests
import json

def get_vlille():
    url = """https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&rows=3000&facet=libelle&facet=nom&facet=commune&facet=etat&facet=type&facet=etatconnexion"""

    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf-8'))
    return response_json.get("records", [])

print(get_vlille())