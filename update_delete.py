##### Imports
from pymongo import MongoClient
from dotenv import load_dotenv
import os

def update_delete(stations):
    ##### Loop 
    CONTINUE = True
    VILLES = ["Lille", "Lyon", "Paris", "Rennes"]

    while CONTINUE :
        action = input("(U)pdate / (D)elete\n").upper()
        ville = int(input("Dans quelle ville souhaitez vous faire vos modifications ? 1-Lille  2-Lyon 3-Paris 4-Rennes\n"))

        cursor = list(stations.find({'city' : VILLES[ville-1]}).sort([("name", 1)]))
        print("Liste des stations de la ville")
        # afficher les 2 premiers individus
        for index, rep in enumerate(cursor):    
            if ville == 2 :
                pos1 = rep['name'].find('-')
                print(f"{index+1} - {rep['name'][pos1+2:]}")
            else : 
                print(f"{index+1} - {rep['name']}")

        if action == 'U' :
            numStation = int(input("Quelle station voulez-vous mettre à jour ? (Entrez le N° de la station)\n"))
            choix = int(input("Souhaitez-vous : \n\t1-Changer le nom de la station \n\t2-Changer la capacité de la station\n"))
            if choix == 1 : 
                newName = input("Entrez le nouveau nom de la station\n")
                stations.update_one({'name' : str(cursor[numStation-1]['name'])}, {"$set" : {'name' : newName}})
                print(f"La station {cursor[numStation-1]['name']} devient {newName}")

            else : 
                newCapacity = int(input("Entrez la nouvelle capacité de la station\n"))
                stations.update_one({'name' : str(cursor[numStation-1]['name'])}, {"$set" : {'size' : newCapacity}})
                print(f"La station {cursor[numStation-1]['name']} a une nouvelle capacité, de {cursor[numStation-1]['size']} à {newCapacity}")

        else : 
            numStation = int(input("Quelle station souhaitez-vous supprimer ? (Entrez le N° de la station)\n"))
            stations.delete_one({'name' : str(cursor[numStation-1]['name'])})
            print(f"La station {cursor[numStation-1]['name']} a bien été supprimée")
        
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
    stations = db["stations"]

    update_delete(stations)
