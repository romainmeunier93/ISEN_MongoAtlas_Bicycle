def map_stations_data(station):
    return {
        "name": station['fields']['nom'], 
        "geometry": {
            "type": "Point",
            "coordinates": station['fields']['localisation']
        },
        "size": station['fields']['nbvelosdispo'] + station['fields']['nbplacesdispo'], 
        "tpe": station['fields']['type'] == "AVEC TPE", 
        "available": station['fields']['etat'] == "EN SERVICE", 
        "city": 'Lille', 
        "municipality": station['fields']['commune']
    }

def map_stations_live_data(station):
    return {
        "name": station['fields']['nom'], 
        "geometry": {
            "type": "Point",
            "coordinates": station['fields']['localisation']
        }, 
        "size": station['fields']['nbvelosdispo'] + station['fields']['nbplacesdispo'], 
        "tpe": station['fields']['type'] == "AVEC TPE", 
        "available": station['fields']['etat'] == "EN SERVICE", 
        "city": 'Lille', 
        "municipality": station['fields']['commune'],
        "available_bikes": station['fields']['nbvelosdispo'],
        "available_stands": station['fields']['nbplacesdispo'],
        "last_update": station["fields"]['datemiseajour']
    }