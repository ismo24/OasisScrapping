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


# Writing a create_table_query
def create_table_scraping_cars():
    try:
        connection = create_connection()
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS SCRAPING_CARS (
            id INT AUTO_INCREMENT PRIMARY KEY,
            webid VARCHAR(50) UNIQUE,
            mark VARCHAR(20),
            model VARCHAR(20),
            price INT,
            annee DATE,
            pays VARCHAR(30),
            transmission VARCHAR(20),
            kilometrage INT,
            carburant VARCHAR(20),
            carosserie VARCHAR(20),
            moteur VARCHAR(20),
            portes INT,
            sieges INT,
            color VARCHAR(20),
            generalValues TEXT,
            basicData TEXT,
            historicalData TEXT,
            technicaData TEXT,
            energieData TEXT,
            equipement TEXT,
            colorData TEXT,
            image_urls TEXT
        );
        """
        cursor.execute(create_table_query)
        connection.commit()
        print("cars table created successfully")

        if connection.is_connected():
            connection.close()
        print("Connection to MySQL DB closed")

    except Error as e:
        print(f"The error '{e}' occurred")




# Writing a create_table_query
def create_table_car():
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
            pays VARCHAR(30),
            transmission VARCHAR(20),
            kilometrage INT,
            carburant VARCHAR(20),
            carosserie VARCHAR(20),
            moteur VARCHAR(20),
            portes INT,
            sieges INT,
            color VARCHAR(20),
            generalValues TEXT,
            basicData TEXT,
            historicalData TEXT,
            technicaData TEXT,
            energieData TEXT,
            equipement TEXT,
            colorData TEXT,
            image_urls TEXT
        );
        """
        cursor.execute(create_table_query)
        connection.commit()
        print("cars table created successfully")

        if connection.is_connected():
            connection.close()
        print("Connection to MySQL DB closed")

    except Error as e:
        print(f"The error '{e}' occurred")


def create_table(query):
    """Create a table from the query provided."""
    connection = create_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            print("Table created successfully")

        except Error as e:
            print(f"The error '{e}' occurred")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")


def create_popular_cars_table():
    """Create the PopularCars table."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS POPULAR_CARS (
        id INT AUTO_INCREMENT PRIMARY KEY,
        webid VARCHAR(50) UNIQUE,
        mark VARCHAR(20),
        model VARCHAR(20),
        price INT,
        generalValues TEXT,
        basicData TEXT,
        historicalData TEXT,
        technicaData TEXT,
        energieData TEXT,
        equipement TEXT,
        colorData TEXT,
        image_urls TEXT
    );
    """
    create_table(create_table_query)

def create_best_deal_cars_table():
    """Create the BestDealCars table."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS BEST_DEAL_CARS (
        id INT AUTO_INCREMENT PRIMARY KEY,
        webid VARCHAR(50) UNIQUE,
        mark VARCHAR(20),
        model VARCHAR(20),
        price INT,
        generalValues TEXT,
        basicData TEXT,
        historicalData TEXT,
        technicaData TEXT,
        energieData TEXT,
        equipement TEXT,
        colorData TEXT,
        image_urls TEXT
    );
    """
    create_table(create_table_query)


def create_static_data_table():
    """Create the StaticData table."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS STATIC_DATA (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title TEXT,
        date TEXT,
        content TEXT
    );
    """
    create_table(create_table_query)


def create_global_stats_table():
    """Create the GlobalStats table."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS GLOBAL_STATS (
        id INT AUTO_INCREMENT PRIMARY KEY,
        mark VARCHAR(20),
        model VARCHAR(20),
        clics INT DEFAULT 0,
        favorites INT DEFAULT 0,
        messages INT DEFAULT 0,
        calls INT DEFAULT 0
    );
    """
    create_table(create_table_query)


def create_cars_stats_table():
    """Create the CarsStats table."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS CARS_STATS (
        id INT AUTO_INCREMENT PRIMARY KEY,
        webid VARCHAR(50) UNIQUE,
        mark VARCHAR(20),
        model VARCHAR(20),
        price INT,
        generalValues TEXT,
        basicData TEXT,
        historicalData TEXT,
        technicaData TEXT,
        energieData TEXT,
        equipement TEXT,
        colorData TEXT,
        image_urls TEXT,
        clics INT,
        clicsDates DATE,
        favorites INT,
        favoritesDates DATE,
        messages INT,
        messagesDates DATE,
        calls INT,
        callsDates DATE
    );
    """
    create_table(create_table_query)

def create_clients_data_table():
    """Create the ClientsData table."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS CLIENTS_DATA (
        id INT AUTO_INCREMENT PRIMARY KEY,
        clientID VARCHAR(20),
        recherches TEXT,
        clics TEXT,
        favorites TEXT,
        messages TEXT,
        calls TEXT,
        recommended TEXT
    );
    """
    create_table(create_table_query)


def create_all_tables():
    create_table_scraping_cars()
    create_table_car()
    create_clients_data_table()
    create_cars_stats_table()
    create_global_stats_table()
    create_static_data_table()
    create_best_deal_cars_table()
    create_popular_cars_table()


def truncate_tables():
    try:
        # Establish connection to the database
        connection = create_connection()
        cursor = connection.cursor()

        # Truncate the table
        truncate_table_query = "TRUNCATE TABLE SCRAPING_CARS;"
        cursor.execute(truncate_table_query)
        connection.commit()
        print("SCRAPING_CARS table truncated successfully")
        # truncate_table_query = "TRUNCATE TABLE cars;"
        # cursor.execute(truncate_table_query)
        # connection.commit()
        # print("cars table truncated successfully")
        # truncate_table_query = "TRUNCATE TABLE CLIENTS_DATA;"  
        # cursor.execute(truncate_table_query)
        # connection.commit()
        # print("CLIENTS_DATA table truncated successfully")

        # truncate_table_query = "TRUNCATE TABLE GLOBAL_STATS;"
        # cursor.execute(truncate_table_query)
        # connection.commit()  
        # print("GLOBAL_STATS table truncated successfully")

        # truncate_table_query = "TRUNCATE TABLE CARS_STATS;"
        # cursor.execute(truncate_table_query)
        # connection.commit()
        # print("CARS_STATS table truncated successfully")

        # truncate_table_query = "TRUNCATE TABLE POPULAR_CARS;"
        # cursor.execute(truncate_table_query)
        # connection.commit()
        # print("POPULAR_CARS table truncated successfully")
        # truncate_table_query = "TRUNCATE TABLE BEST_DEAL_CARS;"
        # cursor.execute(truncate_table_query)
        # connection.commit()
        # print("BEST_DEAL_CARS table truncated successfully")




        # Close the connection if it's open
        if connection.is_connected():
            connection.close()
        print("Connection to MySQL DB closed")

    except Error as e:
        print(f"The error '{e}' occurred")



#Tables à créer 
#'CLIENTS_DATA', GLOBAL_STATS,CARS_STATS,cars,STATIC_DATA,POPULAR_CARS,BEST_DEAL_CARS,

# Create all tables
# create_all_tables()


#truncate tables
truncate_tables()