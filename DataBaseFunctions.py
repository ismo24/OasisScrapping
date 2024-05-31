import requests
import json
from Constants import AllModels

databaseUrl="https://oasis-auto-83872-default-rtdb.europe-west1.firebasedatabase.app"

def getAllAutos():
    url=f"{databaseUrl}/AllIds/AllIds.json"
    response=requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {}
   

def updateAllAutos(AllInfos, token,mylastModel):
    autosLength = len(AllInfos)
    url = f"{databaseUrl}/AllIds/AllIds.json?auth={token}"
    response = requests.patch(url, json=AllInfos, verify=True)  # Enable SSL verification

    print("SuccessfulUpdate ? :", response.status_code == 200)
    print("Total number of cars recorded:", autosLength)

    # try:
    #     response_data = response.json()
    #     print(response_data)
    # except json.JSONDecodeError as e:
    #     print("Failed to decode JSON response:", e)
    #     print("Raw response text:", response.text)
    if response.status_code == 200:
        data={}
        # Charger le fichier JSON
        with open('progression.json', 'r') as file:
            data = json.load(file)
            #Afficher l'index passé
            print("Index passé",data["index"])
            # Modifier les données
            data["index"] = AllModels.index(mylastModel)
            #Afficher l'index présent
            print("Index présent",data["index"])
        # Enregistrer les modifications
        with open('progression.json', 'w') as file:
            json.dump(data, file, indent=4)










