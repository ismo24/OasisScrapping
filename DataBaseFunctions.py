import requests


databaseUrl="https://oasis-auto-83872-default-rtdb.europe-west1.firebasedatabase.app"

def getAllAutos():
    url=f"{databaseUrl}/AllIds/AllIds.json"
    response=requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {}
   

def updateAllAutos(AllInfos):
    autosLength=len(AllInfos)
    url=f"{databaseUrl}/AllIds/AllIds.json"
    response=requests.put(url, json=AllInfos)
    
    print("voitures ajoutées :",autosLength)



def showAutosLength():
    url=f"{databaseUrl}/AllIds/AllIds.json"
    response=requests.get(url)
    resultat=response.json()
    print("nombre de vehicules",len(response.json()))
    modeles=[resultat[i]["model"] for i in resultat.keys() ]
    uniquesmodels=set(modeles)
    print("tous les modeles entrés",uniquesmodels)


# showAutosLength()