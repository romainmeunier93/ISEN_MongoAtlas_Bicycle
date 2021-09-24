import map_vlille_data, map_veloV_data, map_veloRennes_data, map_velib_data
from get_velo import get_velo

from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Déclaration des villes avec des vélos
villes = ["Lille", "Paris", "Lyon", "Rennes"]
getMapping = [map_vlille_data,  map_velib_data, map_veloV_data, map_veloRennes_data]

# Paramétrage du client pour insertion en base de données
load_dotenv()
client = MongoClient(
    "mongodb+srv://" 
    + os.environ.get("DB_USER")
    + ":"
    + os.environ.get("DB_PASSWORD")
    + "@"
    + os.environ.get("DB_CLUSTER")
    + "/"
    + os.environ.get("DB_DATABASE")
    + "?retryWrites=true&w=majority")

db = client[os.environ.get("DB_DATABASE")]
stations = db["stations"]

print(db)
print(stations)

# On parcourt les différentes villes pour mettre à jour la base de données
for index, ville in enumerate(villes) :
    print(f"\n\n****************************************** {ville} ******************************************")
    response = get_velo(ville, getMapping[index].map_stations_data)
    print(f"Nombre de stations : {len(response)}")
    print(response)

    stations.insert_many(response)
