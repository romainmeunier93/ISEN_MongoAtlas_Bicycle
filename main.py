##### Imports
from pymongo import MongoClient
from dotenv import load_dotenv
import os

from update_delete import update_delete
from  ratio import ratio 
from find_station_by_name import find_station_by_name

##### Mango Client 
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
stations_data = db["stations_data"]

CONTINUE = True
while CONTINUE : 
    choix = int(input("Que voulez-vous faire ? \n\t1-Chercher une station \n\t2-Update-delete a station \n\t3-Deactivate all station in an area \n\t4-Station with ratio less than 0.2\n"))

    if choix == 1 :
        find_station_by_name(stations)
    elif choix == 2 :
        update_delete(stations)

    elif choix == 3 :
        print("toto")
    elif choix == 4 :
        ratio(stations_data)

    CONTINUE = True if input("Souhaitez vous continuer ? (O)ui / (N)on \n").upper() == 'O' else False 