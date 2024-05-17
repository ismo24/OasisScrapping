import json
import requests
import re
from Constants import dict_Marques_Names,Auto_models
from ScrapingFunctions import ModelsInfosFinder,price_finder,Infos_generales_Finder,Basic_Data_Finder,Historical_Data_Finder,Technical_Data_Finder,Energie_Data_Finder,Equipment_Data_Finder,Color_Data_Finder
from DataBaseFunctions import getAllAutos,updateAllAutos
from bs4 import BeautifulSoup




AllInfos={}
for marque in dict_Marques_Names.keys():
    marqueKey=f"{marque}"
    for realmodelName,model in Auto_models[marqueKey].items():
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
            OnlineAutos.update(ModelAllInfos)
            updateAllAutos(OnlineAutos)
            
        # else:
        #     print(f"Il n'y a pas de véhicule de la marque {marque} et modèle {model} disponible ")


