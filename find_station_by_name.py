from pymongo import MongoClient
from dotenv import load_dotenv
import os

def find_station_by_name(collection):
    user_text = input("Entrer votre recherche : ")
    query_result = collection.find({
        "$text": {
            "$search": user_text
        }
    },
    {
        "name": 1,
        "city": 1
    })

    stations = list(query_result)

    # print(stations)

    print("Voici le résultat de votre recherche")

    for index, station in enumerate(stations): 
        print(index + 1, "-", station['name'], "- Ville :", station["city"])


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

    find_station_by_name(stations)

