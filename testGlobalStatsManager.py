import random
from GlobalSqlStatsManager import create_global_stat_table,add_new_global_stat_year_model,update_global_stat,update_existing_global_stat_year_model


marks = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan", "BMW", "Mercedes", "Audi", "Volkswagen", "Hyundai"]
models = ["ModelA", "ModelB", "ModelC", "ModelD", "ModelE", "ModelF", "ModelG", "ModelH", "ModelI", "ModelJ"]
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]






#Crér la base de données
create_global_stat_table()


#Insérer 20 voitures à la suite
def generate_and_insert_data():
    for _ in range(20) :
        mark = random.choice(marks)
        model = random.choice(models)
        year = random.choice(years)
        action = random.choice(["clicks", "favorites", "messages", "calls"])
        
        infos = {
            "action": action,
            "data": {
                "mark": mark,
                "model": model,
                "year": year
            }
        }

        update_global_stat(infos)