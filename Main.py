import json
import requests
import re
import os
from bs4 import BeautifulSoup
from Constants import dict_Marques_Names,Auto_models
from ScrapingFunctions import ModelsInfosFinder,price_finder,Infos_generales_Finder,Basic_Data_Finder,Historical_Data_Finder,Technical_Data_Finder,Energie_Data_Finder,Equipment_Data_Finder,Color_Data_Finder
# from DataBaseFunctions import getAllAutos,updateAllAutos
from Authenticate import sign_up,login
from Constants import AllModels
from SqlFunctions import retrieve_to_add_autos,retrieve_to_delete_autos,insert_cars,delete_cars,create_table,delete_table


AllInfos={}
LastModel=[]
lastModelIndex=0
actualModelIndex=0

# Create sql cars database
delete_table("cars")  
create_table()   

for marque in dict_Marques_Names.keys():
    marqueKey=f"{marque}"
    for realmodelName,model in Auto_models[marqueKey].items():
        print("ActuelModel",[marque,realmodelName])

        # Now read the file
        with open('progression.json', 'r') as file:
            data = json.load(file)
            lastModelIndex = data["index"]
        print("lastregisredIndex",lastModelIndex)
        #Retrouver l'index du modèle actuel
        ActuelModel=[marque,realmodelName]
        actualModelIndex=AllModels.index(ActuelModel)
        # Afficher l'index actuel
        print("actuelIndex",actualModelIndex)
        
        #Si l'indice actuel est antérieur au précédent on passe au modèle suivant:
        if actualModelIndex <= lastModelIndex:
            print("modèle déja enregistré on passe au suivant")
            continue


        url_to_scrape=f"https://www.autoscout24.fr/lst/{marque}/{model}?atype=C&cy=D&damaged_listing=exclude&fregfrom=2005&powertype=kw&pricefrom=1000&page=1"
        ModelAllInfos=ModelsInfosFinder(url_to_scrape)

        


        if ModelAllInfos:
            #Enregistrer l'ensemble des Ids dans une liste
            auto_ids=[i for i in ModelAllInfos.keys()]

            # Déterminer la liste des nouvelles voitures à ne pas chercher et à celles à chercher et ajouter
            autos_not_to_search,autos_to_add=retrieve_to_add_autos(auto_ids) 
            # Déterminer la liste des anciennes voitures à enlever
            autos_to_delete=retrieve_to_delete_autos(auto_ids,[marque,model])  

            #Supprimer des voitures à enlever si y'en a:
            delete_cars(autos_to_delete) 

            #supprimer toutes les entrées à ne pas chercher
            for id in autos_not_to_search:
                del ModelAllInfos[id]

            print("Debut de la recherche des informations par véhicules")  
            
            for autoId in autos_to_add:
                # print("autoId :",autoId)
                auto_url = f"https://www.autoscout24.fr/offres/{autoId}"
                auto_response = requests.get(auto_url)
                auto_data = auto_response.text
                # Parse le contenu HTML avec BeautifulSoup
                auto_soup = BeautifulSoup(auto_data, 'html.parser')

                GeneralValues=Infos_generales_Finder(auto_soup)
                BasicData=Basic_Data_Finder(auto_soup)
                ColorData=Color_Data_Finder(auto_soup)

                ModelAllInfos[autoId]["price"]=price_finder(auto_soup)
                ModelAllInfos[autoId]["generalValues"] = GeneralValues["Infos_finales"] if GeneralValues and  "Infos_finales" in GeneralValues else None
                ModelAllInfos[autoId]["kilometrage"] = GeneralValues["Kilométrage"] if GeneralValues and "Kilométrage" in GeneralValues else None
                ModelAllInfos[autoId]["carburant"] = GeneralValues["Carburant"] if GeneralValues and "Carburant" in GeneralValues else None
                ModelAllInfos[autoId]["annee"] = GeneralValues["Année"] if GeneralValues and "Année" in GeneralValues else None
                ModelAllInfos[autoId]["transmission"] = GeneralValues["Transmission"] if GeneralValues and "Transmission" in GeneralValues else None

                ModelAllInfos[autoId]["basicData"] = BasicData["Infos_finales"] if BasicData and "Infos_finales" in BasicData else None
                ModelAllInfos[autoId]["carosserie"] = BasicData["Carrosserie"] if BasicData and "Carrosserie" in BasicData else None
                ModelAllInfos[autoId]["sieges"] = BasicData["Sièges"] if BasicData and "Sièges" in BasicData else None
                ModelAllInfos[autoId]["portes"] = BasicData["Portes"] if BasicData and "Portes" in BasicData else None
                ModelAllInfos[autoId]["pays"] = BasicData["pays"] if BasicData and "pays" in BasicData else None
                ModelAllInfos[autoId]["moteur"] = BasicData["Type de moteur"] if BasicData and "Type de moteur" in BasicData else None


                ModelAllInfos[autoId]["historicalData"]=Historical_Data_Finder(auto_soup)
                ModelAllInfos[autoId]["technicaData"]=Technical_Data_Finder(auto_soup)
                ModelAllInfos[autoId]["energieData"]=Energie_Data_Finder(auto_soup)
                ModelAllInfos[autoId]["equipement"]=Equipment_Data_Finder(auto_soup)

                ModelAllInfos[autoId]["colorData"]=ColorData["Infos_finales"] if ColorData and "Infos_finales" in ColorData else None
                ModelAllInfos[autoId]["color"]=ColorData["Couleur"]  if ColorData and "Couleur" in ColorData else None

                ModelAllInfos[autoId]["mark"]=dict_Marques_Names[marque]
                ModelAllInfos[autoId]["model"]=realmodelName
                

            if len(ModelAllInfos)>2:
                print(ModelAllInfos)
                
            
                
                
            # OnlineAutos=getAllAutos()
            # print("ancien nombre de voitures :",len(OnlineAutos))
            # print(f"voitures à ajouter {marque} :",len(ModelAllInfos))
            # New_dict={**OnlineAutos,**ModelAllInfos}
            # OnlineAutos.update(ModelAllInfos)
            # print('nouvelle longueur normalement :',len(OnlineAutos))
            # updateAllAutos(ModelAllInfos,myToken,actualModelIndex)

            insert_cars(ModelAllInfos,actualModelIndex)

            
        else:
            print(f"Il n'y a pas de véhicule de la marque {marque} et modèle {model} disponible ")


