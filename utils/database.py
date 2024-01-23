import mysql.connector
from mysql.connector import Error

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '12345',
    'database': 'utility_management_system'
}

def connect_to_database():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Connected to MySQL database.")
            return connection
    except Error as e:
        print("Error while connecting to MySQL:", e)
        return None

def close_database_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Connection to MySQL database closed.")

