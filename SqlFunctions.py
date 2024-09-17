import mysql.connector
from mysql.connector import Error
import json

# Establish a Connection to the MySQL Database
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='ismo',  # Replace with your MySQL username
            password='2359Koura@ismael',  # Replace with your MySQL password '2359@Koura','2359Koura@ismael'
            database='cars_store'  # Replace with your database name
        )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


# Create a Function to Execute a Query
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")



# Create a Function to Fetch Results from a Query

def fetch_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")





def insert_cars(all_infos, actualModelIndex):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        car_query = """                                                                             
        INSERT INTO SCRAPING_CARS (webid, mark, model, price, annee, pays, transmission, kilometrage, carburant, carosserie, moteur, portes, sieges, color, generalValues, basicData, historicalData, technicaData, energieData, equipement, colorData, image_urls) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        InsertionsLength = len(all_infos)
        
        for car_id, car_info in all_infos.items():
            values = (
                car_id,
                car_info.get("mark", None),
                car_info.get("model", None),
                car_info.get("price", None),
                car_info.get("annee", None),
                car_info.get("pays", None),
                car_info.get("transmission", None),
                car_info.get("kilometrage", None),
                car_info.get("carburant", None),
                car_info.get("carosserie", None),
                car_info.get("moteur", None),
                car_info.get("portes", None),
                car_info.get("sieges", None),
                car_info.get("color", None),
                json.dumps(car_info.get("generalValues", [])),
                json.dumps(car_info.get("basicData", [])),
                json.dumps(car_info.get("historicalData", [])),
                json.dumps(car_info.get("technicaData", [])),
                json.dumps(car_info.get("energieData", [])),
                json.dumps(car_info.get("equipement", [])),
                json.dumps(car_info.get("colorData", [])),
                json.dumps(car_info.get("image_urls", [])),
            )
            cursor.execute(car_query, values)
            connection.commit()
        print(f"{InsertionsLength} autos inserted successfully")
        if connection.is_connected():
            connection.close()
            print("Connection to MySQL DB closed")

        data = {"index": actualModelIndex}
        print("Index modifié", data["index"])
        # Enregistrer les modifications
        with open('progression.json', 'w') as file:
            json.dump(data, file, indent=4)
    except Error as e:
        print(f"The error '{e}' occurred")


# Example usage
# insert_cars(ModelAllInfos, actualModelIndex)


import sqlite3

def get_carsis_cars_webids():
    try:
        # Connexion à la base de données SQLite
        connection = create_connection()
        cursor = connection.cursor()

        # Requête SQL pour récupérer les webids contenant 'Carsis_cars'
        query = "SELECT webid FROM cars WHERE webid LIKE '%Carsis_cars%'"

        # Exécution de la requête et récupération des résultats
        cursor.execute(query)
        results = cursor.fetchall()
        
        # Fermer la connexion à la base de données
        
        if connection.is_connected():
            connection.close()
            print("Connection to MySQL DB closed")

        # Retourner les webids sous forme de liste
        return [row[0] for row in results]
    except Error as e:
        print(f"The error '{e}' occurred")




def insert_carsis_sellers_car(auto_webid,car_info):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        car_query = """                                                                             
        INSERT INTO cars (webid, mark, model, price, annee, pays, transmission, kilometrage, carburant, carosserie, moteur, portes, sieges, color, generalValues, basicData, historicalData, technicaData, energieData, equipement, colorData, image_urls) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        
        values = (
                auto_webid,
                car_info.get("mark", None),
                car_info.get("model", None),
                car_info.get("price", None),
                car_info.get("annee", None),
                car_info.get("pays", None),
                car_info.get("transmission", None),
                car_info.get("kilometrage", None),
                car_info.get("carburant", None),
                car_info.get("carosserie", None),
                car_info.get("moteur", None),
                car_info.get("portes", None),
                car_info.get("sieges", None),
                car_info.get("color", None),
                json.dumps(car_info.get("generalValues", [])),
                json.dumps(car_info.get("basicData", [])),
                json.dumps(car_info.get("historicalData", [])),
                json.dumps(car_info.get("technicaData", [])),
                json.dumps(car_info.get("energieData", [])),
                json.dumps(car_info.get("equipement", [])),
                json.dumps(car_info.get("colorData", [])),
                json.dumps(car_info.get("image_urls", [])),
            )
        cursor.execute(car_query, values)
        connection.commit()
        print(f"car {auto_webid}  inserted successfully")
        if connection.is_connected():
            connection.close()
            print("Connection to MySQL DB closed")

    except Error as e:
        print(f"The error '{e}' occurred")

def delete_carsis_seller_records():
    try:
        # Connexion à la base de données SQLite
        connection = create_connection()
        cursor = connection.cursor()

        # Requête SQL pour supprimer les enregistrements dont le webid contient 'Carsis_Seller'
        delete_query = "DELETE FROM cars WHERE webid LIKE '%Carsis_cars%'"

        # Exécution de la requête de suppression
        cursor.execute(delete_query)
        connection.commit()  # Confirmer la suppression des enregistrements
        
        print(f"{cursor.rowcount} records deleted successfully.")

        # Fermer la connexion à la base de données
        if connection:
            connection.close()
            print("Connection to MySQL DB closed")
    except Error as e:
        print(f"The error '{e}' occurred")


# function to delete a list of cars
def delete_cars(car_ids):
    if car_ids==[]:
        return
   
    try:
        connection = create_connection()
        cursor = connection.cursor()
        # Construct the SQL query
        format_strings = ','.join(['%s'] * len(car_ids))
        query = f"DELETE FROM SCRAPING_CARS WHERE webid IN ({format_strings})"
        
        # Execute the query
        cursor.execute(query, tuple(car_ids))
        connection.commit()
        print(f"{cursor.rowcount} records deleted successfully")

        if connection.is_connected():
            connection.close()
        print("Connection to MySQL DB closed")

    except Error as e:
        print(f"The error '{e}' occurred")

    

    

def retrieve_to_add_autos(ids):
    existing_ids = []
    non_existing_ids = []

    try:
        connection = create_connection()
        cursor = connection.cursor()
        # Prepare the SQL query to check for existing IDs
        format_strings = ','.join(['%s'] * len(ids))
        query = f"SELECT webid FROM SCRAPING_CARS WHERE webid IN ({format_strings})"
        cursor.execute(query, tuple(ids))
        
        # Fetch all results
        result = cursor.fetchall()
        result_ids = [row[0] for row in result]
        
        # Separate existing and non-existing IDs
        for id in ids:
            if id in result_ids:
                existing_ids.append(id)
            else:
                non_existing_ids.append(id)

        if connection.is_connected():
            connection.close()
            print("Connection to MySQL DB closed")

    except Error as e:
        print(f"The error '{e}' occurred")
    
    return existing_ids,non_existing_ids



def retrieve_to_delete_autos(ids,searchValues):
    existing_ids = []
    to_delete_ids= []

    try:
        connection = create_connection()
        cursor = connection.cursor()
        # Prepare the SQL query search for corresponding autos
        
        query = f"SELECT webid FROM SCRAPING_CARS WHERE mark = %s AND model = %s;"

        cursor.execute(query,(searchValues[0], searchValues[1]))
        
        # Fetch all results
        result = cursor.fetchall()
        result_ids = [row[0] for row in result]
        
        # Separate existing and non-existing IDs
        for id in result_ids:
            if id in ids:
                existing_ids.append(id)
            else:
                to_delete_ids.append(id)

        if connection.is_connected():
            connection.close()
            print("Connection to MySQL DB closed")

    except Error as e:
        print(f"The error '{e}' occurred")
    
    return to_delete_ids


