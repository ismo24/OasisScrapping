from SqlFunctions import create_connection
import mysql.connector
from mysql.connector import Error
import json



#Créer une base de données qui reccueuile les statistiques globales des clients basés sur leures interactions
def create_global_stat_table():
    try: 
        connection = create_connection()
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS GLOBAL_STATS (
            id INT AUTO_INCREMENT PRIMARY KEY,
            mark VARCHAR(20),
            model VARCHAR(20),
            year YEAR,
            clicks INT,
            favorites INT,
            messages INT,
            calls INT
        );
        """
        # Execute the query
        cursor.execute(create_table_query)
        connection.commit()
        print("Table created successfully")

        if connection.is_connected():
            connection.close()
        print("Connection to MySQL DB closed")

    except Error as e:
        print(f"The error '{e}' occurred")



infos={
    "action":"clicks,favorites,messages,calls",
    "data":{
        "mark":"mark",
        "model":"model",
        "year":"year"
    }
}


def update_global_stat(infos):
    try:
        # Create connection and connect to cursor
        connection = create_connection()
        cursor = connection.cursor()
        action=infos["action"]

        # Verify if year_model_exist
        year_model_data=get_year_model_in_global_stat(connection, infos["data"])
        if(not year_model_data):
            add_new_global_stat_year_model(connection, infos)
        else:
            modifyingIndex=["clicks", "favorites", "messages", "calls"].index(action)
            print("receivedValues :",year_model_data)
            prev_value=year_model_data[modifyingIndex+4]
            model_year_id=year_model_data[0]
            update_existing_global_stat_year_model(connection,model_year_id,action,prev_value)

        
        print("Global update successfully")

        if connection.is_connected():
            connection.close()
        print("Connection to MySQL DB closed")

    except Error as e:
        print(f"The error '{e}' occurred")


#function pour retrouver un modèle de données si il est dans la base de données

def get_year_model_in_global_stat(connection, data):
    try:
        cursor = connection.cursor()

        # Extract the values from the data dictionary
        mark = data.get("mark",None)
        model = data.get("model",None)
        year = data.get("year",None)

        # Construct the query with placeholders for parameters
        query = """
        SELECT * FROM GLOBAL_STATS WHERE mark = %s AND model = %s AND year = %s
        """

        # Execute the query with the actual values from the data dictionary
        cursor.execute(query, (mark, model, year))

        # Fetch all matching records
        results = cursor.fetchall()

        # Close the cursor
        cursor.close()

        print("get_year_model_in_global_stat successfully")
        return results[0]
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


 
# Créer une méthode pour ajouter des valeurs à cette table 

def update_existing_global_stat_year_model(connection, model_year_id, action, prev_value):
    try:
        cursor = connection.cursor()

        print("model_year_id :",model_year_id,"action :",action,"prev_value :",prev_value)
        # Prepare the query with placeholders
        query = f"""
        UPDATE GLOBAL_STATS 
        SET {action} = %s
        WHERE id = %s;
        """

        # Calculate the new value
        new_value = prev_value + 1

        print("new_value :",new_value)

        # Execute the query with parameterized values
        cursor.execute(query, (new_value, model_year_id))
        connection.commit()

        print("update_existing_global_stat_year_model successfully")
        
    except Exception as e:
        print(f"The error '{e}' occurred")
    finally:
        if cursor:
            cursor.close()


#function pour ajouter un nouveau modele de vehicule qui n'est pas dans la table global_stat

def add_new_global_stat_year_model(connection, infos):
    try:
        cursor = connection.cursor()
        
        # Extract data and action from infos
        data = infos.get("data", {})
        action = infos.get("action", "")
        
        # Prepare the values list, inserting None for missing data
        values = [
            data.get("mark", None),
            data.get("model", None),
            data.get("year", None),
            0,  # clicks
            0,  # favorites
            0,  # messages
            0   # calls
        ]
        
        # Determine the index of the action to set the corresponding value to 1
        action_index = ["clicks", "favorites", "messages", "calls"].index(action)
        values[3 + action_index] = 1  # Adjust for the offset of the first three columns
        
        # Prepare the query with placeholders
        query = """
        INSERT INTO GLOBAL_STATS (mark, model, year, clicks, favorites, messages, calls) 
        VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        
        # Execute the query
        cursor.execute(query, values)
        connection.commit()
        
        print("add_new_global_stat_year_model successfully")

    except Exception as e:
        print(f"The error '{e}' occurred")
    finally:
        if cursor:
            cursor.close()






def display_all_global_stats():
    try:
        # Create connection and connect to cursor
        connection = create_connection()
        cursor = connection.cursor()

        # Construct the query to fetch all columns from GLOBAL_STATS
        query = """
        SELECT * FROM GLOBAL_STATS
        """

        # Execute the query
        cursor.execute(query)

        # Fetch all rows
        results = cursor.fetchall()

        # Fetch column names
        column_names = [i[0] for i in cursor.description]

        # Print column names
        print(" | ".join(column_names))

        # Print each row
        for row in results:
            print(" | ".join(str(col) for col in row))

    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        if cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()
        print("Connection to MySQL DB closed")



def delete_all_values_from_global_stats():
    try:
        # Create connection and connect to cursor
        connection = create_connection()
        cursor = connection.cursor()

        # Construct the query to delete all rows from GLOBAL_STATS
        query = "DELETE FROM GLOBAL_STATS"

        # Execute the query
        cursor.execute(query)
        connection.commit()

        print("All values deleted successfully")

    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        if cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()
        print("Connection to MySQL DB closed")