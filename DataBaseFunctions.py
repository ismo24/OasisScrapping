import requests
import json


databaseUrl="https://oasis-auto-83872-default-rtdb.europe-west1.firebasedatabase.app"

def getAllAutos():
    url=f"{databaseUrl}/AllIds/AllIds.json"
    response=requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {}
   

def updateAllAutos(AllInfos, token):
    autosLength = len(AllInfos)
    url = f"{databaseUrl}/AllIds/AllIds.json?auth={token}"
    response = requests.patch(url, json=AllInfos, verify=True)  # Enable SSL verification

    print("SuccessfulUpdate ? :", response.status_code == 200)
    print("Total number of cars recorded:", autosLength)

    try:
        response_data = response.json()
        print(response_data)
    except json.JSONDecodeError as e:
        print("Failed to decode JSON response:", e)
        print("Raw response text:", response.text)


