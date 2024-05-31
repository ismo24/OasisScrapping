import json
import requests
import re
import os
from bs4 import BeautifulSoup
from Constants import dict_Marques_Names,Auto_models
from ScrapingFunctions import ModelsInfosFinder,price_finder,Infos_generales_Finder,Basic_Data_Finder,Historical_Data_Finder,Technical_Data_Finder,Energie_Data_Finder,Equipment_Data_Finder,Color_Data_Finder
from DataBaseFunctions import getAllAutos,updateAllAutos
from Authenticate import sign_up,login
from Constants import AllModels



AllInfos={}
LastModel=[]
myToken=login()
lastModelIndex=0


    

for marque in dict_Marques_Names.keys():
    marqueKey=f"{marque}"
    for realmodelName,model in Auto_models[marqueKey].items():
        print("ActuelModel",[marque,realmodelName])
        # Indexer la valeur du dernier modèle terminé 
        # Charger le fichier JSON
        # Check if the file exists
        file_path = 'progression.json'
        if not os.path.exists(file_path):
            # Create the file with initial content
            print("the file don't exist")
            with open(file_path, 'w') as file:
                json.dump({"index": 6}, file)

        # Now read the file
        with open(file_path, 'r') as file:
            data = json.load(file)
            lastModelIndex = data["index"]
        print("lastregisredIndex",lastModelIndex)
        #Retrouver l'index du modèle actuel
        ActuelModel=[marque,realmodelName]
        actualModelIndex=AllModels.index(ActuelModel)
        # Afficher l'index actuel
        print("actuelIndex",actualModelIndex)
        
        #Si l'indice actuel est antérieur au précédent on passe au modèle suivant:
        if actualModelIndex < lastModelIndex:
            print("modèle déja enregistré on passe au suivant")
            continue


        url_to_scrape=f"https://www.autoscout24.fr/lst/{marque}/{model}?atype=C&cy=D&damaged_listing=exclude&fregfrom=2005&powertype=kw&pricefrom=3000&page=1"
        ModelAllInfos=ModelsInfosFinder(url_to_scrape)

        if ModelAllInfos:
            print("Debut de la recherche des informations par véhicules")
            for autoId in ModelAllInfos.keys():
                # print("autoId :",autoId)
                auto_url = f"https://www.autoscout24.fr/offres/{autoId}"
                auto_response = requests.get(auto_url)
                auto_data = auto_response.text
                # Parse le contenu HTML avec BeautifulSoup
                auto_soup = BeautifulSoup(auto_data, 'html.parser')
                ModelAllInfos[autoId]["myPrice"]=price_finder(auto_soup)
                ModelAllInfos[autoId]["myGeneralValues"]=Infos_generales_Finder(auto_soup)
                ModelAllInfos[autoId]["myBasicData"]=Basic_Data_Finder(auto_soup)
                ModelAllInfos[autoId]["myHistoricalData"]=Historical_Data_Finder(auto_soup)
                ModelAllInfos[autoId]["myTechnicaData"]=Technical_Data_Finder(auto_soup)
                ModelAllInfos[autoId]["myEnergieData"]=Energie_Data_Finder(auto_soup)
                ModelAllInfos[autoId]["myEquipement"]=Equipment_Data_Finder(auto_soup)
                ModelAllInfos[autoId]["myColorData"]=Color_Data_Finder(auto_soup)
                ModelAllInfos[autoId]["marque"]=marque
                ModelAllInfos[autoId]["model"]=realmodelName
                
                # print("nouveau vehicule :",ModelAllInfos[autoId])
                
            OnlineAutos=getAllAutos()
            print("ancien nombre de voitures :",len(OnlineAutos))
            print(f"voitures à ajouter {marque} :",len(ModelAllInfos))
            # New_dict={**OnlineAutos,**ModelAllInfos}
            # OnlineAutos.update(ModelAllInfos)
            # print('nouvelle longueur normalement :',len(OnlineAutos))
            
            updateAllAutos(ModelAllInfos,myToken,ActuelModel)
            
        # else:
        #     print(f"Il n'y a pas de véhicule de la marque {marque} et modèle {model} disponible ")


