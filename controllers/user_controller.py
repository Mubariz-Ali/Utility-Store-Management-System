from utils.database import connect_to_database, close_database_connection


def register_user(username, password):
    connection = connect_to_database()
    if not connection:
        return None

    new_user = None
    try:
        cursor = connection.cursor(dictionary=True)
        insert_query = "INSERT INTO user (username, password) VALUES (%s, %s)"
        cursor.execute(insert_query, (username, password))
        connection.commit()
    finally:
        if cursor:
            cursor.close()
            close_database_connection(connection)
    return new_user
