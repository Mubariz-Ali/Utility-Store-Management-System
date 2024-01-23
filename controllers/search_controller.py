from models.item import Item
from utils.database import connect_to_database, close_database_connection
from mysql.connector import Error


def search_by_name(item_name):
    connection = connect_to_database()
    if not connection:
        return None

    searched_item = None

    try:
        cursor = connection.cursor(dictionary=True)
        search_query = "SELECT * FROM utilityitem WHERE item_name = %s"
        cursor.execute(search_query, (item_name,))
        searched_item = cursor.fetchone()

    except Error as e:
        print("Error while executing query:", e)

    finally:
        if cursor:
            cursor.close()
            close_database_connection(connection)

    return searched_item


def search_by_id(item_id):
    connection = connect_to_database()
    if not connection:
        return None

    searched_item = None
    try:
        cursor = connection.cursor(dictionary=True)
        search_query = "SELECT * FROM utilityitem WHERE item_id = %s"
        cursor.execute(search_query, (item_id,))
        searched_item = cursor.fetchone()

    except Error as e:
        print("Error while executing query:", e)

    finally:
        if cursor:
            cursor.close()
            close_database_connection(connection)

    return searched_item
