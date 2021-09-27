def map_stations_data(station):
    return {
        "name": station['fields']['nom'], 
        "geometry": {
            "type": "Point",
            "coordinates": station['fields']['coordonnees']
        },
        "size": station['fields']['nombreemplacementsactuels'], 
        "available": station['fields']['etat'] == 'En fonctionnement', 
        "city": 'Rennes'
    }

def map_stations_live_data(station):
    return {
        "name": station['fields']['nom'], 
        "geometry": {
            "type": "Point",
            "coordinates": station['fields']['coordonnees']
        },
        "size": station['fields']['nombreemplacementsactuels'], 
        "available": station['fields']['etat'] == 'En fonctionnement', 
        "city": 'Rennes',
        "available_bikes": station['fields']['nombrevelosdisponibles'],
        "available_stands": station['fields']['nombreemplacementsdisponibles'],
        "last_update": station['fields']['lastupdate']
    }