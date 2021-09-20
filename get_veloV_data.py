import requests
import json

def get_veloV():
    url = "https://transport.data.gouv.fr/gbfs/lyon/station_information.json"

    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf-8'))
    return response_json.get("data", [])

print(get_veloV())
