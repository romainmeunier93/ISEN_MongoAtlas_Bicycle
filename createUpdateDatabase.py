import get_vlille_data, get_veloV_data, get_veloRennes_data, get_velib_data

from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Déclaration des villes avec des vélos
villes = ["Lille", "Paris", "Lyon", "Rennes"]
getFiles = [get_vlille_data, get_velib_data, get_veloV_data, get_veloRennes_data]

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
    response = getFiles[index].get_velo() 
    print(f"Nombre de stations : {len(response)}")
    print(response)

    stations.insert_many(response)
