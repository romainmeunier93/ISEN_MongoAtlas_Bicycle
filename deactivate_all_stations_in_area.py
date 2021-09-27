from pymongo import MongoClient
from dotenv import load_dotenv
import os

def deactivate_stations_in_area(collection):

    center_point = input("Entrer les coordonées du centre de la zone à désactiver ( sous la forme ( longitude, latitude ) : ")

    long = float(center_point.split(',')[0])
    lat = float(center_point.split(',')[1])

    radius = input("Entrer le rayon de la zone à désactiver (en mètres) : ")

    query_result = collection.aggregate([
        {
            "$geoNear": { 
                "near": {
                    "type": "Point", 
                    "coordinates": [float(long), float(lat)]
                }, 
                "maxDistance": int(radius),
                "query": {},
                "spherical": "true", 
                "distanceField": "calcDistance"
            }
        },
        {
            "$project": {
                "_id": 1,
                "name": 1
            }
        }
    ])

    concerned_stations = list(query_result)
    concerned_stations_ids = [record['_id'] for record in concerned_stations]

    update_result = collection.update_many({
        "_id": {
            "$in": concerned_stations_ids
        }
    },
    {
        "$set": {
            "available": False
        }
    })

    print(update_result.modified_count, "stations ont été modifiées.")
    if update_result.modified_count > 0:
        print("Stations modifiées ou inchangées : ")
        for index, station in enumerate(concerned_stations):
            print(index + 1, "-", station['name'])

if __name__ == "__main__":
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

    deactivate_stations_in_area(stations)