
from SqlFunctions import insert_carsis_sellers_car,get_carsis_cars_webids,delete_carsis_seller_records
from carsis_seller_autos_models.Lexus_RX_350.file import Lexus_RX_350
from carsis_seller_autos_models.Lexus_NX_200t.file import Lexus_NX_200t
from carsis_seller_autos_models.Hyundai_TUCSON.file import Hyundai_TUCSON
from carsis_seller_autos_models.Hyundai_TUCSON_Limited.file import Hyundai_TUCSON_Limited
from carsis_seller_autos_models.Hyundai_ELANTRA.file import Hyundai_ELANTRA   
from carsis_seller_autos_models.Hyundai_SANTA_FE.file import Hyundai_SANTA_FE    
from carsis_seller_autos_models.Kia_Optima.file import Kia_OPTIMA  
from carsis_seller_autos_models.Kia_Sportage.file import Kia_SPORTAGE   
from carsis_seller_autos_models.Kia_Sportage_Limited.file import Kia_SPORTAGE_Limited 
from carsis_seller_autos_models.Toyota_RAV_4.file import Toyota_RAV_4  
from carsis_seller_autos_models.Toyota_RAV_4_LE.file import Toyota_RAV_4_LE
from carsis_seller_autos_models.Toyota_RAV_4_Limited.file import Toyota_RAV4_Limited
from carsis_seller_autos_models.Toyota_RAV_4_Sport.file import Toyota_RAV4_Sport
from carsis_seller_autos_models.Toyota_RAV_4_XLE.file import Toyota_RAV4_XLE



all_autos=[*Hyundai_TUCSON,*Hyundai_TUCSON_Limited,*Hyundai_ELANTRA,*Hyundai_SANTA_FE,
           *Kia_OPTIMA,*Kia_SPORTAGE,*Kia_SPORTAGE_Limited,*Toyota_RAV_4,
           *Toyota_RAV_4_LE,*Toyota_RAV4_Limited,*Toyota_RAV4_Sport,*Toyota_RAV4_XLE]  #*Lexus_RX_350,*Lexus_NX_200t,



import random
import string




# for auto in all_autos:
#     insert_carsis_sellers_car(auto)

webids=[]       
for auto in all_autos:
    webids.append(auto['webid'])

print('arrayLength: ',len(webids))
print('SetLength: ', len(set(webids)))

# print("carsis_sellers_length :",len(all_autos))
#for testing each automels

# for auto in Hyundai_ELANTRA:
#     existing_strings = get_carsis_cars_webids()
#     unique_string = generate_unique_string(existing_strings)
#     if(unique_string):
#         print(unique_string)
#         insert_carsis_sellers_car(unique_string,auto) 


#function to delete Carsis records
# delete_carsis_seller_records()
