def map_stations_data(station):
    return {
        "name": station['name'], 
        "geometry": {
            "type": "Point",
            "coordinates": station['position']
        }, 
        "size": station['totalStands']['capacity'], 
        "tpe": station['banking'], 
        "available": station['status'] == 'OPEN', 
        "city": 'Lyon'
    }

def map_stations_live_data(station):
    return {
        "name": station['name'], 
        "geometry": {
            "type": "Point",
            "coordinates": station['position']
        },
        "size": station['totalStands']['capacity'], 
        "tpe": station['banking'], 
        "available": station['status'] == 'OPEN', 
        "city": 'Lyon',
        "available_bikes": station['totalStands']['availabilities']['bikes'],
        "available_stands": station['totalStands']['availabilities']['stands'],
        "last_update": station['lastUpdate']
    }