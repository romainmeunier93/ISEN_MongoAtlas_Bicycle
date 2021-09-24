from pymongo import MongoClient
from dotenv import load_dotenv
import os
import time

import map_vlille_data, map_veloV_data, map_veloRennes_data, map_velib_data
from get_velo import get_velo

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

while True :
    print(f"\n\n****************************************** RENNES ******************************************")
    response = get_velo("Rennes", map_veloRennes_data.map_stations_live_data) 
    print(f"Nombre de stations : {len(response)}")
    # print(response)

    stations_data.insert_many(response)

    time.sleep(120)

