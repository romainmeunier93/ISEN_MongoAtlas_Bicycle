def map_stations_data(station):
    return {
        "name": station['fields']['name'], 
        "geometry": {
            "type": "Point",
            "coordinates": station['fields']['coordonnees_geo']
        },
        "size": station['fields']['capacity'], 
        "available": station['fields']['is_renting'] == "OUI", 
        "city": 'Paris', 
        "municipality": station['fields']['nom_arrondissement_communes']
    }

def map_stations_live_data(station):
    return {
        "name": station['fields']['name'], 
        "geometry": {
            "type": "Point",
            "coordinates": station['fields']['coordonnees_geo']
        },
        "size": station['fields']['capacity'], 
        "available": station['fields']['is_renting'] == "OUI", 
        "city": 'Paris', 
        "municipality": station['fields']['nom_arrondissement_communes'],
        "available_bikes": station['fields']['numbikesavailable'],
        "available_stands": station['fields']['numdocksavailable'],
        "last_update": station['fields']['duedate']
    }