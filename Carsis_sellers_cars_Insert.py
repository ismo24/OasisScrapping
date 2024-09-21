
from SqlFunctions import insert_carsis_sellers_car,get_carsis_cars_webids,delete_carsis_seller_records
from carsis_seller_autos_models.Lexus_RX_350.file import Lexus_RX_350
from carsis_seller_autos_models.Lexus_NX_200t.file import Lexus_NX_200t
from carsis_seller_autos_models.Hyundai_TUCSON.file import Hyundai_TUCSON
from carsis_seller_autos_models.Hyundai_TUCSON_Limited.file import Hyundai_TUCSON_Limited
from carsis_seller_autos_models.Hyundai_ELANTRA.file import Hyundai_ELANTRA



all_autos=[*Lexus_RX_350,*Lexus_NX_200t,*Hyundai_TUCSON,*Hyundai_TUCSON_Limited,*Hyundai_ELANTRA]



import random
import string

def generate_unique_string(existing_strings):
    prefix = "Carsis_cars"
    suffix_length = 20 - len(prefix)  # Calculer la longueur du suffixe à générer

    while True:
        # Générer un suffixe aléatoire de longueur appropriée
        suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=suffix_length))
        
        # Combiner le préfixe et le suffixe pour créer la chaîne unique
        new_string = prefix + suffix
        
        # Vérifier si le nouveau string est déjà dans la liste
        if new_string not in existing_strings:
            return new_string

# Exemple d'utilisation


for auto in all_autos:
    existing_strings = get_carsis_cars_webids()
    unique_string = generate_unique_string(existing_strings)
    if(unique_string):
        print(unique_string)
        insert_carsis_sellers_car(unique_string,auto)

print("carsis_sellers_length :",len(auto))
#for testing each automels

# for auto in Hyundai_ELANTRA:
#     existing_strings = get_carsis_cars_webids()
#     unique_string = generate_unique_string(existing_strings)
#     if(unique_string):
#         print(unique_string)
#         insert_carsis_sellers_car(unique_string,auto) 


#function to delete Carsis records
# delete_carsis_seller_records()
