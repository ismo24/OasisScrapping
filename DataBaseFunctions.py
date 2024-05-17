import requests


databaseUrl="https://oasis-auto-83872-default-rtdb.europe-west1.firebasedatabase.app"

def getAllAutos():
    url=f"{databaseUrl}/AllIds/AllIds.json"
    response=requests.get(url)
    
    # return response.json()
   





def updateAllAutos(AllInfos):
    autosLength=len(AllInfos)
    url=f"{databaseUrl}/AllIds/AllIds.json"
    response=requests.patch(url, json=AllInfos)
    
    print("voitures ajoutées :",autosLength)





