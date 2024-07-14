


import json
import requests
import re
from bs4 import BeautifulSoup






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
        return price

    except ValueError as ve:
        print(f"Erreur de valeur : {ve}")
        return False
    except Exception as e:
        print(f"Erreur inattendue : {e}")
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

        if Infos_finales:
            return Infos_finales
        else:
            return False
    
    except ValueError as ve:
        print(f"Erreur de valeur : {ve}")
        return False
    except Exception as e:
        print(f"Erreur inattendue : {e}")
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
            return Infos_finales
        else:
            return False
        
    
    except ValueError as ve:
        print(f"Erreur de valeur : {ve}")
        return False
    except Exception as e:
        print(f"Erreur inattendue : {e}")
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
        print(f"Erreur de valeur : {ve}")
        return False
    except Exception as e:
        print(f"Erreur inattendue : {e}")
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
        print(f"Erreur de valeur : {ve}")
        return False
    except Exception as e:
        print(f"Erreur inattendue : {e}")
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
        print(f"Erreur de valeur : {ve}")
        return False
    except Exception as e:
        print(f"Erreur inattendue : {e}")
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
        print(f"Erreur de valeur : {ve}")
        return False
    except Exception as e:
        print(f"Erreur inattendue : {e}")
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
            return Infos_finales
        else:
            return False

    except ValueError as ve:
        print(f"Erreur de valeur : {ve}")
        return False
    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return False