import requests
from Authenticate import sign_up,login





myToken=login()

databaseUrl="https://oasis-auto-83872-default-rtdb.europe-west1.firebasedatabase.app"

def showAutosLength():
    url=f"{databaseUrl}/AllIds/AllIds.json"
    response=requests.get(url)
    resultat=response.json()
    # print("nombre de vehicules",len(response.json()))
    # total=0
    # for id in resultat.keys():
    #     for idkeys in resultat[id].keys():
    #         if idkeys=="modèle":
    #             resultat[id]["model"]=resultat[id]["modèle"]
    #             del resultat[id]["modèle"]
    #             total+=1
    #             break
    # print("nombre modifié",total)
    # url=f"{databaseUrl}/AllIds/AllIds.json"
    # response=requests.put(url, json=resultat)
    
    modeles=[resultat[i]["model"] for i in resultat.keys() if resultat[i]["marque"]=='volkswagen' ]
    uniquesmodels=set(modeles)
    print("tous les modeles entrés",uniquesmodels)


showAutosLength()


myDict={'C 250', 'X7', 'i3', 'Grand C-Max', 'Allroad', 'C 55 AMG', 'Transit Connect', 'GT', 'E 550', 'a8', 'AMG GT', 'Série 4 (tous)', 'R8', '216', '220', 'X3', 'Focus CC', 'A6 allroad', 'RS5', 'E 50 AMG', 'C 200', 'A5', 'A 180', 'Classe C (tous)', 'B 150', '225', 'Série M (tous)', 'iX2', 'A 170', 'A6', 'Grand Tourneo', 'Mondeo', '130', 'Transit Custom', 'A4', 'Tourneo Courier', '300', '350', 'M850', 'CL 55 AMG', '316', '750', '230', 'C 240', '620', '540', '528', 'CL 600', 'Kuga', '180', 'Active Hybrid 3', 'e-tron', 'S4', 'i5', '116', 'Transit', 'TTS', 'i7',
         '428', '650', 'C 180', 'F 150', 'iX3', 'X1', '430', 'RS Q3', 'a4-allroad', 'E 240', 'Galaxy', 'S3', 'X7 M', 'S6', 'i8', 'A 250', 'A 200', 'Escape', 'Série X (tous)', 'Cabriolet', 'S1', 'Edge', 'Maverick', 'Citan', 'X5 M', 'E 55 AMG', 'E 270', '640', '760', 'a7', 'Flex', 'X6', 'Q5', 'Oreon', 'Tourneo', 'EcoSport', 'A 45 AMG', 'B Electric Drive', 'Transit Bus', 'M550', 'Crown', 'Série Z (tous)', 'X2 M', 'XM', 'SQ7', 'CLA 220', 'S240', 'Taurus', 'a2', '550', 'M4', 'QUATTRO', 'Q4 e-tron', 'C 280', 'Grant Torino', '635', '228', 'Prob', 'Transit Courier', 'B 160', 'CLA 35 AMG', 'A 160', 'G 300', 'Coupe', 'Active Hybrid 7', 'E 280', 'S7', 'Ranger Raptor', 'SQ5', 'SQ8 e-tron', 'M5', '525', 'TT-RS', 'Atego', 'RS', 'CL 180', '210/310', 'X4', '118', 'RS6', '125', 'A 220', 'Q8 e-tron', 'a5', '320', 'RS e-tron GT', '418', 'B 250', 'CL 220', 'E 420', 'X4 M', 'Focus', '740', 'i4', 'V8', 'Série 3 (tous)', 'A 150', '250', 'CL 230', '645', '318', 'SQ6', 'e-tron GT', 'Série 5 (tous)', '735', 'Q2', '140', 'Mustang', 'B-MAX', '114', 'Ka/Ka+', 'CL 63 AMG', 'A4 allroad', 'CLA 180',
           'Explorer', 'F 350', '200', '123', '328', 'Z4', 'TT', 'Tourneo Custom', 'C 350', 'S5', '450', '518', 'A 35 AMG', 'C 450', '120', 'M', 'RS3', 'S-Max', 'iX', '1er M Coupé', '335', '840', '425', '850', 'A7', 'X5', '170', 'a3', 'a4', '330', 'Ranger (tous)', 'Streetka', 'Tourneo Connect', 'A2', 'Fiesta', 'Puma', 'CLA 200', '530', 'a1', '420', '135', '440', 'Bronco', 'C 220', '535', 'Fusion', 'C 43 AMG', 'F 250', '523', 'A1', '235', '50', '280', 'M2', 'A8', 'RS Q8', 'X6 M', 'CL 500', 'C 230', '214', '500', 'Scorpio', '340', 'X2', '223', 'C 320', 'M8', '730', 'Série 8 (tous)', 'Autres', 'RS4', 'X3 M', 'Q8', 'C 400', 'B 170', 'S8', 'a6', 'B 180', 'Q3', '745', '325', 'CLA 45 AMG', 'C-MAX', 'Actros', '218', 'iX1', 'B 220', '128', 'B 200', 'CLA 250', 'SQ2', '545', 'Focus C-Max', 'Courier', 'C 270', 'A3', '435', 'M1', '630', 'a6-allroad', 'E 230', 'Z4 M', 'SQ8', '520', 'C 300', 'M6', 'Q7', 'E-Transit', 'Mustang Mach-E', 'M3', 'Ranger', 'Expedition', 'RS7'}


def testget():
    url=f"{databaseUrl}/Test/Test.json"
    response=requests.get(url)
    print("SuccesssfullGet ? :",response.status_code == 200)
    resultat=response.json()
    print("test",resultat)

def testUpdate(token):
    url=f"{databaseUrl}/Test/Test.json?auth={token}"
    response=requests.patch(url,json={'f':5,'g':6,'h':7,'i':8})
    print("SuccesssfullUpdate ? :",response.status_code == 200)
    resultat=response.json()
    print("test",resultat)


# testUpdate(myToken)
# testget()