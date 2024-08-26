from SqlFunctions import create_connection
import mysql.connector
from mysql.connector import Error
import json

def countCars():
        try:
            connection = create_connection()
            cursor = connection.cursor()
            # Prepare the SQL query to count all entries
            query = "SELECT COUNT(*) FROM cars;"
            cursor.execute(query)
            
            # Fetch the result
            result = cursor.fetchone()
            car_count = result[0]
            print("Total cars :",car_count)
            return car_count
        except Error as e:
            print(f"The error '{e}' occurred")
            return None
        

def countScrapingCars():
        try:
            connection = create_connection()
            cursor = connection.cursor()
            # Prepare the SQL query to count all entries
            query = "SELECT COUNT(*) FROM SCRAPING_CARS;"
            cursor.execute(query)
            
            # Fetch the result
            result = cursor.fetchone()
            car_count = result[0]
            print("Total scraping_cars :",car_count)
            return car_count
        except Error as e:
            print(f"The error '{e}' occurred")
            return None
        




def fetchSomeCars ():
    try:
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        # Préparez la requête SQL pour sélectionner les 10 premières entrées
        query = "SELECT * FROM cars LIMIT 10;"
        cursor.execute(query)
        
        # Récupérez tous les résultats
        results = cursor.fetchall()
        for i in results:
             print(i)
        return results
    except Error as e:
        print(f"Une erreur '{e}' est survenue")
        return None
    

def fetchSomeScrapingCars ():
    try:
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        # Préparez la requête SQL pour sélectionner les 10 premières entrées
        query = "SELECT * FROM SCRAPING_CARS LIMIT 10;"
        cursor.execute(query)
        
        # Récupérez tous les résultats
        results = cursor.fetchall()
        for i in results:
             print(i)
        return results
    except Error as e:
        print(f"Une erreur '{e}' est survenue")
        return None


countScrapingCars()
countCars()  
fetchSomeCars ()
fetchSomeScrapingCars ()