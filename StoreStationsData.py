import get_vlille_data, get_veloV_data, get_veloRennes_data, get_velib_data

from pymongo import MongoClient
from dotenv import load_dotenv
import os, time

# Déclaration des villes avec des vélos
ville = "Rennes"
getFile = get_veloRennes_data

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
stations_data = db["stations_data"]

print(db)
print(stations_data)

while True :
    print(f"\n\n****************************************** {ville} ******************************************")
    response = get_veloRennes_data.get_velo() 
    print(f"Nombre de stations : {len(response)}")
    print(response)

    stations_data.insert_many(response)

    time.sleep(120)
