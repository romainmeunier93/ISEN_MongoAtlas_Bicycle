import requests
import json

def mapNames(station):
    return {"Name": station['name'], "Coordinates": station['position'], "Size": station['totalStands']['capacity'], "TPE": station['banking'], "Available": station['status'], "City": 'Lyon'}

def get_velo():
    url = "https://api.jcdecaux.com/vls/v3/stations?apiKey=frifk0jbxfefqqniqez09tw4jvk37wyf823b5j1i&contract=lyon"

    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf-8'))
    response = response_json

    return list(map(mapNames, response))