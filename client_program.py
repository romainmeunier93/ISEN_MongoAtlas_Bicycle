from pymongo import MongoClient
from dotenv import load_dotenv
import os

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

user_location = input("Entrer votre localisation ( sous la forme : longitude, latitude ) :")

long = float(user_location.split(',')[0])
lat = float(user_location.split(',')[1])

result = stations_data.aggregate([
    {
        "$geoNear": { 
            "near": {
                "type": "Point", 
                "coordinates": [long, lat]
            }, 
            "query": {
                "available": True
            },
            "spherical": "true", 
            "distanceField": "calcDistance"
        }
    }, 
    {
        "$group": {
            "_id": "$name",
            "name": {"$last": "$name"},
            "available_bikes": {"$last": "$available_bikes"},
            "available_stands": {"$last": "$available_stands"},
            "geometry": {"$last": "$geometry"},
            "calcDistance": {"$last": "$calcDistance"}
        }
    },
    {
        "$sort": {"calcDistance": 1}
    },
    {
        "$limit": 5
    },
    {
        "$project": {
            "_id": 0,
            "name": 1,
            "available_bikes": 1,
            "available_stands": 1,
            "calcDistance": 1
        }
    }
])

stations = list(result)

print("Voici la liste des stations : \n")
for station in stations:
    print("Nom : ", station['name'])
    print("Distance : ", int(station['calcDistance']), "m")
    print("Places disponibles : ", station['available_bikes'])
    print("Emplacements disponibles : ", station['available_stands'], '\n')