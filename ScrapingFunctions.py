


import json
import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime






def ModelsInfosFinder(url_to_scrape):
    try:
        
        url = url_to_scrape
        pageId = 1
        WholeModelInfos = {}
        oldPage = ""

        while True: 
            # Générer le changement de page dans l'URL
            if pageId != 1:
                oldPage = f"&page={pageId - 1}"
                newPage = f"&page={pageId}"
                url = url.replace(oldPage, newPage)
            
            # print(f"Fetching data from: {url}")  # Affiche l'URL utilisée pour le debug

            # Télécharge la page
            response = requests.get(url)
            if response.status_code != 200:
                # print(f"Failed to fetch page with status code: {response.status_code}")
                break
            
            data = response.text

            # Parse le contenu HTML avec BeautifulSoup
            soup = BeautifulSoup(data, 'html.parser')

            # Trouve la balise script avec l'id spécifié
            script_Container = soup.find('script', id='__NEXT_DATA__')
            

            # Extraction des données JSON du contenu de la balise script
            data = json.loads(script_Container.get_text(strip=True))

            # Extraction des IDs de véhicules et images
            vehicles = data['props']['pageProps']['listings']
            
            if not vehicles:
                # print('No More vehicules .')
                break
            for vehicle in vehicles:
                vehicle_id = f"{vehicle['id']}"
                image_urls = [image.replace("/250x188.webp", "") for image in vehicle['images']]
                WholeModelInfos[vehicle_id]={"image_urls":image_urls}  
                # print(f"Vehicle ID: {vehicle_id}")
                # print(f"Image URLs: {image_urls}")

            pageId += 1
            # print("Total vehicles processed:", len(WholeModelInfos))

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    if len(WholeModelInfos) == 0:
        return False
    return WholeModelInfos  # Retourne les informations collectées ou une liste vide en cas d'erreur

    


def price_finder(soup):
    try:
        # Trouve la balise div avec la classe spécifiée pour le conteneur principal de prix
        price_container = soup.find('div', class_='Price_mainPriceContainer__1rI7u')
        if not price_container:
            raise ValueError("Conteneur de prix non trouvé")

        # Trouve la balise span contenant le prix à l'intérieur du conteneur
        price_span = price_container.find('span', class_='PriceInfo_price__XU0aF')
        if not price_span:
            raise ValueError("Balise de prix non trouvée dans le conteneur")

        # Enlever tous les caractères non numériques et convertir le tout en entier
        price = int(re.sub(r'\D', '', price_span.text))

        # Retourrner false si la valeur du véhicule est inférieure à 1000 euros
        if(price<1000):
            return False


        def calculate_price(value):
            converted_price = (int((value * 655) / 1000)) * 1000
            end_price = converted_price

            if converted_price < 3000000:
                end_price += 1200000
            elif converted_price < 8000_000:
                end_price += 1500000
            elif converted_price < 12000000:
                end_price += 2000000
            elif converted_price < 20000000:
                end_price += 2500000
            elif converted_price < 30000000:
                end_price += 3000000
            else:
                end_price += 4000000
            
            print("clientPrice :",end_price)
            return end_price



        return calculate_price(price)

    except ValueError as ve:
        print(f"Erreur de valeur price_finder: {ve}")
        return False
    except Exception as e:
        print(f"Erreur inattendue price_finder: {e}")
        return False

def Infos_generales_Finder(soup):
    try:
        # Trouve la balise div avec la classe spécifiée pour les informations générales
        Infos_Generales_container = soup.find('div', class_='StageArea_overviewContainer__UyZ9n')
        if not Infos_Generales_container:
            raise ValueError("Conteneur des informations générales non trouvé")
        
        # Liste pour stocker les textes trouvés
        titles = []
        values = []
        Infos_finales=[]
        AllInfos={}

        # Trouve toutes les div dont la classe contient 'Title'
        for div in Infos_Generales_container.find_all('div', class_=lambda value: value and 'Title' in value):
            # Ajoute le texte de chaque div à la liste
            titles.append(div.get_text(strip=True).replace('\u202f', ' '))
        
        # Trouve toutes les div dont la classe contient 'Title'
        for div in Infos_Generales_container.find_all('div', class_=lambda value: value and 'Text' in value):
            # Ajoute le texte de chaque div à la liste
            values.append(div.get_text(strip=True).replace('\u202f', ' '))

        # retourner une erreur si le nombre de titres n'est pas égal au nombre de valeurs
        if len(titles)!=len(values):
            raise ValueError("Nombre de titres différents du nombre de valeurs")
        
        # Retourner les valeurs dans une liste adéquate en retirant les informations sur les vendeurs
        for i in range(len(titles)):
            if titles[i]!='Vendeur':
                Infos_finales.append([titles[i],values[i]])

        def transform_to_integer(value):
            # Enlever les caractères non numériques
            value = ''.join(filter(str.isdigit, value))
            # Convertir en entier
            return int(value)
        
        def parse_date(value):
            formats = ["%m/%Y", "%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y", "%Y/%m/%d"]
            
            # Essayer chaque format jusqu'à ce que l'un d'entre eux fonctionne
            for fmt in formats:
                try:
                    date_obj = datetime.strptime(value, fmt).date()
                    return date_obj
                except ValueError:
                    continue
            
            # Si aucun format ne fonctionne, lever une exception
            return None

        if Infos_finales:
            for value in Infos_finales:
                AllInfos["Infos_finales"]=Infos_finales
                if value[0]=="Kilométrage":
                    kilometrage=transform_to_integer(value[1])
                    AllInfos["Kilométrage"]=kilometrage
                if value[0]=="Transmission":
                    AllInfos["Transmission"]=value[1]
                if value[0]=="Année":
                    date_obj = parse_date(value[1])
                    AllInfos["Année"]=date_obj  
                if value[0]=="Carburant":
                    AllInfos["Carburant"]=value[1]
                

            return AllInfos
        else:
            return False
    
    except ValueError as ve:
        print(f"Erreur de valeur Infos_generales_Finder: {ve}")
        return False
    except Exception as e:
        print(f"Erreur inattendue Infos_generales_Finder: {e}")
        return False


def Basic_Data_Finder(soup):

    try:
        # Trouve la balise section avec la classe spécifiée pour les informations basiques
        Basic_Data_container = soup.find('section', id="basic-details-section")
        if not Basic_Data_container:
            raise ValueError("Conteneur des données basiques non trouvé")   
        
        
        # Liste pour stocker les informations  trouvées
        titles = []
        values = []
        Infos_finales=[]
        AllInfos={}  

        # Trouve toutes les dt dont la classe contient 'DataGrid_defaultDtStyle__soJ6R'
        for dt in Basic_Data_container.find_all('dt', class_='DataGrid_defaultDtStyle__soJ6R'):
            # Ajoute le texte de chaque dt
            titles.append(dt.get_text(strip=True).replace('\u202f', ' '))
  
        # Trouve toutes les dd dont la classe contient 'DataGrid_defaultDdStyle__3IYpG DataGrid_fontBold__RqU01'
        for dd in Basic_Data_container.find_all('dd', class_='DataGrid_defaultDdStyle__3IYpG DataGrid_fontBold__RqU01'):
            # Ajoute le texte de chaque dd
            values.append(dd.get_text(strip=True).replace('\u202f', ' '))
        
        # Retourner les valeurs dans une liste adéquate
        for i in range(len(titles)):
            if titles[i]!='Garantie':
                Infos_finales.append([titles[i],values[i]])

        
        if Infos_finales:
            AllInfos["Infos_finales"]=Infos_finales
            for value in Infos_finales:
                if value[0]=="Carrosserie":
                    AllInfos["Carrosserie"]=value[1]  
                if value[0]=="Type de moteur":
                    AllInfos["Type de moteur"]=value[1]
                if value[0]=="Sièges":
                    AllInfos["Sièges"]=value[1]  
                if value[0]=="Portes":
                    AllInfos["Portes"]=value[1]   
                if value[0]=="Version pays":
                    AllInfos["pays"]=value[1]

            return AllInfos
        else:
            return False
        
    
    except ValueError as ve:
        print(f"Erreur de valeur Basic_Data_Finder: {ve}")
        return False
    except Exception as e:
        print(f"Erreur inattendue Basic_Data_Finder: {e}")
        return False




def Historical_Data_Finder(soup):

    try:
        # Trouve la balise section avec l'id spécifiée pour les informations historiques
        Historical_Data_container = soup.find('section', id="listing-history-section")
        if not Historical_Data_container:
            raise ValueError("Conteneur des données historiques non trouvé")  

        # Liste pour stocker les informations  trouvées
        titles = []
        values = []
        Infos_finales=[]

        # Trouve toutes les dt dont la classe contient 'DataGrid_defaultDtStyle__soJ6R'
        for dt in Historical_Data_container.find_all('dt', class_='DataGrid_defaultDtStyle__soJ6R'):
            # Ajoute le texte de chaque dt
            titles.append(dt.get_text(strip=True).replace('\u202f', ' '))

       
        # Trouve toutes les dd dont la classe contient 'DataGrid_defaultDdStyle__3IYpG DataGrid_fontBold__RqU01'
        for dd in Historical_Data_container.find_all('dd', class_='DataGrid_defaultDdStyle__3IYpG DataGrid_fontBold__RqU01'):
            # Ajoute le texte de chaque dd
            values.append(dd.get_text(strip=True).replace('\u202f', ' '))

         # Retourner les valeurs dans une liste adéquate
        for i in range(len(titles)):
            Infos_finales.append([titles[i],values[i]])

        
        if Infos_finales:
            return Infos_finales
        else:
            return False

    except ValueError as ve:
        print(f"Erreur de valeur Historical_Data_Finder: {ve}")
        return False
    except Exception as e:
        print(f"Erreur inattendue Historical_Data_Finder: {e}")
        return False




def Technical_Data_Finder(soup):

    try:
        # Trouve la balise section avec l'id spécifiée pour les informations techniques
        Technical_Data_container = soup.find('section', id="technical-details-section")
        if not Technical_Data_container:
            raise ValueError("Conteneur des données techniques non trouvé")  

        # Liste pour stocker les informations  trouvées
        titles = []
        values = []
        Infos_finales=[]

          # Trouve toutes les dt dont la classe contient 'DataGrid_defaultDtStyle__soJ6R'
        for dt in Technical_Data_container.find_all('dt', class_='DataGrid_defaultDtStyle__soJ6R'):
            # Ajoute le texte de chaque dt
            titles.append(dt.get_text(strip=True).replace('\u202f', ' '))

       
        # Trouve toutes les dd dont la classe contient 'DataGrid_defaultDdStyle__3IYpG DataGrid_fontBold__RqU01'
        for dd in Technical_Data_container.find_all('dd', class_='DataGrid_defaultDdStyle__3IYpG DataGrid_fontBold__RqU01'):
            # Ajoute le texte de chaque dd
            values.append(dd.get_text(strip=True).replace('\u202f', ' '))

        # Retourner les valeurs dans une liste adéquate
        for i in range(len(titles)):
            Infos_finales.append([titles[i],values[i]])

        
        if Infos_finales:
            return Infos_finales
        else:
            return False

    except ValueError as ve:
        print(f"Erreur de valeur Technical_Data_Finder: {ve}")
        return False
    except Exception as e:
        print(f"Erreur inattendue Technical_Data_Finder : {e}")
        return False
    


def Energie_Data_Finder(soup):

    try:
        # Trouve la balise section avec l'id spécifiée pour les informations environnemntales
        Energie_Data_container = soup.find('section', id="environment-details-section")
        if not Energie_Data_container:
            raise ValueError("Conteneur des données environnementales non trouvé")  

        # Liste pour stocker les informations  trouvées
        titles = []
        values = []
        Infos_finales=[]

          # Trouve toutes les dt dont la classe contient 'DataGrid_defaultDtStyle__soJ6R'
        for dt in Energie_Data_container.find_all('dt', class_='DataGrid_defaultDtStyle__soJ6R'):
            # Ajoute le texte de chaque dt
            titles.append(dt.get_text(strip=True).replace('\u202f', ' '))

       
        # Trouve toutes les dd dont la classe contient 'DataGrid_defaultDdStyle__3IYpG DataGrid_fontBold__RqU01'
        for dd in Energie_Data_container.find_all('dd', class_='DataGrid_defaultDdStyle__3IYpG DataGrid_fontBold__RqU01'):
            # Ajoute le texte de chaque dd
            values.append(dd.get_text(strip=True).replace('\u202f', ' '))

        # Retourner les valeurs dans une liste adéquate
        for i in range(len(titles)):
            Infos_finales.append([titles[i],values[i]])

        
        if Infos_finales:
            return Infos_finales
        else:
            return False

    except ValueError as ve:
        print(f"Erreur de valeur Energie_Data_Finder : {ve}")
        return False
    except Exception as e:
        print(f"Erreur inattendue Energie_Data_Finder : {e}")
        return False


def Equipment_Data_Finder(soup):

    try:
        # Trouve la balise section avec l'id spécifiée pour les informations en équipement
        Equipment_Data_container = soup.find('section', id="equipment-section")
        if not Equipment_Data_container:
            raise ValueError("Conteneur des données équipement non trouvé")  

        # Liste pour stocker les informations  trouvées
        titles = []
        values = []
        Infos_finales=[]

          # Trouve toutes les dt dont la classe contient 'DataGrid_defaultDtStyle__soJ6R'
        for dt in Equipment_Data_container.find_all('dt', class_='DataGrid_defaultDtStyle__soJ6R'):
            # Ajoute le texte de chaque dt
            titles.append(dt.get_text(strip=True).replace('\u202f', ' '))

        
        # Trouve toutes les dd dont la classe contient 'DataGrid_defaultDdStyle__3IYpG DataGrid_fontBold__RqU01'
        for dd in Equipment_Data_container.find_all('dd', class_='DataGrid_defaultDdStyle__3IYpG'):
            #Récupères le li contenant les donées
            equipmentValues=dd.find_all('li')
            equipArr=[]
            for li in equipmentValues:
                equipArr.append(li.get_text(strip=True).replace('\u202f', ' '))
            # Ajoute le texte de chaque dd
            values.append(equipArr)

        # Retourner les valeurs dans une liste adéquate
        for i in range(len(titles)):
            Infos_finales.append([titles[i],values[i]])

        
        if Infos_finales:
            return Infos_finales
        else:
            return False

    except ValueError as ve:
        print(f"Erreur de valeur Equipment_Data_Finder: {ve}")
        return False
    except Exception as e:
        print(f"Erreur inattendue Equipment_Data_Finder: {e}")
        return False


def Color_Data_Finder(soup):

    try:
        # Trouve la balise section avec l'id spécifiée pour les informations sur la couleur
        Color_Data_container = soup.find('section', id="color-section")
        if not Color_Data_container:
            raise ValueError("Conteneur des données sur la couleur non trouvé")  

        # Liste pour stocker les informations  trouvées
        titles = []
        values = []
        Infos_finales=[]
        AllInfos={}
        

          # Trouve toutes les dt dont la classe contient 'DataGrid_defaultDtStyle__soJ6R'
        for dt in Color_Data_container.find_all('dt', class_='DataGrid_defaultDtStyle__soJ6R'):
            # Ajoute le texte de chaque dt
            titles.append(dt.get_text(strip=True).replace('\u202f', ' '))

       
        # Trouve toutes les dd dont la classe contient 'DataGrid_defaultDdStyle__3IYpG DataGrid_fontBold__RqU01'
        for dd in Color_Data_container.find_all('dd', class_='DataGrid_defaultDdStyle__3IYpG DataGrid_fontBold__RqU01'):
            # Ajoute le texte de chaque dd
            values.append(dd.get_text(strip=True).replace('\u202f', ' '))

        # Retourner les valeurs dans une liste adéquate
        for i in range(len(titles)):
            Infos_finales.append([titles[i],values[i]])  

        
        if Infos_finales:
            AllInfos["Infos_finales"]=Infos_finales
            for value in Infos_finales:                
                if value[0]=="Couleur extérieure":
                    AllInfos["Couleur"]=value[1]
            return AllInfos
        else:
            return False

    except ValueError as ve:
        print(f"Erreur de valeur Color_Data_Finder: {ve}")
        return False
    except Exception as e:
        print(f"Erreur inattendue Color_Data_Finder: {e}")
        return False