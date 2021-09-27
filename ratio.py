##### Imports
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import datetime

def ratio(stations_data):
    #### Code
    CONTINUE = True

    while CONTINUE :
        ratio = list(stations_data.aggregate(
            [
                {
                    '$set': {
                        'weekday': {
                            '$dayOfWeek': {
                                "$dateFromString" : {
                                    "dateString" : "$last_update"
                                }
                            }
                        },
                        'hour' : {
                            "$hour" :{
                                "$dateFromString" : {
                                    "dateString" : "$last_update"
                                }
                            }
                        }
                    }
                }, {
                    '$match': {
                        'weekday': {
                            '$lte': 6,
                            '$gte': 2
                        },
                        'hour' : {
                            '$lt' : 14,
                            '$gte' : 13
                        }
                    }
                }, {
                    '$group': {
                        '_id': '$name',
                        'sum_available_bikes': {
                            '$sum': '$available_bikes'
                        },
                        'sum_sizes': {
                            '$sum': '$size'
                        }
                    }
                }, {
                    '$set': {
                        'ratio': {
                            '$divide': [
                                '$sum_available_bikes', '$sum_sizes'
                            ]
                        }
                    }
                }, {
                    '$match': {
                        'ratio': {
                            '$lte': 0.2
                        }
                    }
                }, {
                    '$project': {
                        '_id': 1,
                        'ratio': 1
                    }
                }
            ]
        ))

        for station in ratio :
            print(f"{station['_id']} | {round(station['ratio'], 2)} %")

        CONTINUE = True if input("Souhaitez vous continuer ? (O)ui / (N)on \n").upper() == 'O' else False 

    return

if __name__ == "__main__" :
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
    stations_data = db["stations_data"]

    ratio(stations_data)

