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
            password='2359Koura@ismael',  # Replace with your MySQL password
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


# Writing a create_table_query
def create_table():
    try: 
        connection = create_connection()
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS cars (
            id INT AUTO_INCREMENT PRIMARY KEY,
            webid VARCHAR(50) UNIQUE,
            mark VARCHAR(20),
            model VARCHAR(20),
            price INT,
            annee DATE,
            pays  VARCHAR(30),
            transmission VARCHAR(20),
            kilometrage INT,
            carburant  VARCHAR(20),
            carosserie VARCHAR(20),
            moteur VARCHAR(20),
            portes INT,
            sieges INT,
            color VARCHAR(20),
            generalValues TEXT,
            basicData TEXT,
            historicalData TEXT,
            technicaData  TEXT,
            energieData  TEXT,
            equipement  TEXT,
            colorData  TEXT,
            image_urls TEXT,
            clics INT,
            clicsDates TEXT,
            messages  INT,
            messagesDates TEXT,
            calls INT,
            callsDates TEXT,
        );
        """
        # Execute the query
        cursor.execute(create_table_query)
        connection.commit()
        print("cars table created successfully")

        if connection.is_connected():
            connection.close()
        print("Connection to MySQL DB closed")

    except Error as e:
        print(f"The error '{e}' occurred")


def delete_table(table_name):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        # Prepare the SQL query to drop the table
        query = f"DROP TABLE IF EXISTS {table_name};"
        
        cursor.execute(query)
        connection.commit()
        print(f"Table `{table_name}` deleted successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Connection to MySQL DB closed")


# function to insert a list of cars informations
def insert_cars (all_infos,actualModelIndex):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        car_query = """                                                                             
        INSERT INTO cars (webid, mark, model, price, annee, pays, transmission, kilometrage, carburant, carosserie, moteur, portes, sieges, color, generalValues, basicData, historicalData, technicaData, energieData, equipement, colorData, image_urls,clics,clicsDates,messages,messagesDates,calls,callsDates) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        InsertionsLength=len(all_infos)
        
        for car_id in all_infos.keys():
            values=(
            car_id,
            all_infos[car_id]["mark"] if all_infos[car_id]["mark"] else None,
            all_infos[car_id]["model"] if all_infos[car_id]["model"] else None,
            all_infos[car_id]["price"] if all_infos[car_id]["price"] else None,
            all_infos[car_id]["annee"] if all_infos[car_id]["annee"] else None,
            all_infos[car_id]["pays"] if all_infos[car_id]["pays"] else None,
            all_infos[car_id]["transmission"] if all_infos[car_id]["transmission"] else None,
            all_infos[car_id]["kilometrage"] if all_infos[car_id]["kilometrage"] else None,
            all_infos[car_id]["carburant"] if  all_infos[car_id]["carburant"] else None,
            all_infos[car_id]["carosserie"] if all_infos[car_id]["carosserie"] else None,
            all_infos[car_id]["moteur"] if all_infos[car_id]["moteur"] else None,
            all_infos[car_id]["portes"] if all_infos[car_id]["portes"] else None,
            all_infos[car_id]["sieges"] if all_infos[car_id]["sieges"] else None,
            all_infos[car_id]["color"] if all_infos[car_id]["color"] else None,


            json.dumps(all_infos[car_id]["generalValues"]) if all_infos[car_id]["generalValues"] else None,
            json.dumps(all_infos[car_id]["basicData"]) if all_infos[car_id]["basicData"] else None,
            json.dumps(all_infos[car_id]["historicalData"]) if all_infos[car_id]["historicalData"] else None,
            json.dumps(all_infos[car_id]["technicaData"]) if all_infos[car_id]["technicaData"] else None,
            json.dumps(all_infos[car_id]["energieData"]) if all_infos[car_id]["energieData"] else None,
            json.dumps(all_infos[car_id]["equipement"]) if all_infos[car_id]["equipement"] else None,
            json.dumps(all_infos[car_id]["colorData"]) if all_infos[car_id]["colorData"] else None,
            json.dumps(all_infos[car_id]["image_urls"]) if all_infos[car_id]["image_urls"] else None,
            0,
            "[]",
            0,
             "[]", 
              0,
             "[]",    
            )
            cursor.execute(car_query, values)
            connection.commit()
        print(f" {InsertionsLength} autos inserted successfully")
        if connection.is_connected():
            connection.close()
            print("Connection to MySQL DB closed")

        data={"index": actualModelIndex}
        print("Index modifié",data["index"])
        # Enregistrer les modifications
        with open('progression.json', 'w') as file:
            json.dump(data, file, indent=4)
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
        query = f"DELETE FROM cars WHERE webid IN ({format_strings})"
        
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
        query = f"SELECT webid FROM cars WHERE webid IN ({format_strings})"
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
        
        query = f"SELECT webid FROM cars WHERE mark = %s AND model = %s;"

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


