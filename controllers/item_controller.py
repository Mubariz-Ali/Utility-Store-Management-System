from models.item import Item
from utils.database import connect_to_database, close_database_connection
from mysql.connector import Error


def get_all_items():
    connection = connect_to_database()
    if not connection:
        return None

    item = None
    try:
        cursor = connection.cursor(dictionary=True)
        item_query = "SELECT * FROM utilityitem"
        cursor.execute(item_query)
        items = cursor.fetchall()
        allItems = []

        if (items):
            for item in items:
                currentItem = Item(item['item_id'], item['item_name'], item['description'], item['unit_price'],
                                   item['quantity_in_stock'], item['category'])
                allItems.append(currentItem)

    except Error as e:
        print("Error while executing query:", e)
    finally:
        if cursor:
            cursor.close()
        close_database_connection(connection)

    return allItems


def item_to_add(self, item_id, item_name, category, description, unit_price, quantity_in_stock):
    connection = connect_to_database()
    if not connection:
        return None

    added_item = None
    try:
        cursor = connection.cursor()
        add_query = "INSERT INTO utilityitem (item_id, item_name, category, description, unit_price, " \
                    "quantity_in_stock) " \
                    "VALUES (%s, %s, %s, %s, %s, %s)"
        # item_to_add = (item_id, item_name, category, description, unit_price, quantity_in_stock)
        cursor.execute(add_query, (item_id, item_name, category, description, unit_price, quantity_in_stock))
        connection.commit()
    finally:
        if cursor:
            cursor.close()
            close_database_connection(connection)
            return added_item


def item_to_delete(item_id):
    connection = connect_to_database()
    if not connection:
        return None

    deleted_item = None
    try:
        cursor = connection.cursor()
        delete_query = "DELETE FROM utilityitem WHERE item_id = %s"
        cursor.execute(delete_query, (item_id,))
        connection.commit()
    finally:
        if cursor:
            cursor.close()
            close_database_connection(connection)

            return deleted_item


def item_to_update(self, item_id, new_item_name, new_category, new_description, new_unit_price):
    connection = connect_to_database()
    if not connection:
        return None

    updated_item = None
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM utilityitem WHERE item_id = %s", (item_id,))
        existing_item = cursor.fetchone()
        if not existing_item:
            return None

        update_query = "UPDATE utilityitem SET item_name = %s, category = %s, description = %s, unit_price = %s " \
                       " WHERE item_id = %s"
        updated_item = (new_item_name, new_category, new_description, new_unit_price, item_id)
        cursor.execute(update_query, updated_item)
        # cursor.execute(update_query, item_id, new_item_name, new_category, new_description, new_unit_price)
        connection.commit()
        updated_item = cursor.fetchone()

    finally:
        if cursor:
            cursor.close()
            close_database_connection(connection)

    return updated_item


def sell_item(self, item_id, quantity_sold, sale_date):
    connection = connect_to_database()
    if not connection:
        return None

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM utilityitem WHERE item_id = %s", (item_id,))
        existing_item = cursor.fetchone()
        if not existing_item:
            return None

        quantity_in_stock = existing_item[4]
        if quantity_in_stock < quantity_sold:
            return None

        unit_price = existing_item[3]
        new_unit_price = float(unit_price) + (float(unit_price) * float(0.25))
        total_cost = new_unit_price * quantity_sold

        new_quantity = quantity_in_stock - quantity_sold
        selling_query = "UPDATE utilityitem SET quantity_in_stock = %s WHERE item_id = %s"
        sale_data = (new_quantity, item_id)
        cursor.execute(selling_query, sale_data)

        sale_query = "INSERT INTO sale (item_id, sale_date, quantity_sold, total_price) VALUES (%s, %s, %s, " \
                     "%s)"
        sold_data = (item_id, sale_date, quantity_sold, total_cost)
        cursor.execute(sale_query, sold_data)
        connection.commit()

        return total_cost
    except Error as e:
        return None
    finally:
        if cursor:
            cursor.close()
            close_database_connection(connection)


def purchase_item(self, item_id, purchased_quantity, purchase_date):
    connection = connect_to_database()
    if not connection:
        return None

    cursor = None
    try:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM utilityitem WHERE item_id = %s", (item_id,))
        existing_item = cursor.fetchone()
        if not existing_item:
            return None

        unit_price = existing_item[3]
        total_cost = unit_price * purchased_quantity

        new_quantity = existing_item[4] + purchased_quantity  # Index 4 corresponds to quantity_in_stock
        update_query = "UPDATE utilityitem SET quantity_in_stock = %s WHERE item_id = %s"
        update_data = (new_quantity, item_id)
        cursor.execute(update_query, update_data)

        purchase_query = "INSERT INTO purchase (item_id, quantity_purchased,  purchase_date,  total_price) " \
                         "VALUES (%s, %s, %s, %s)"
        purchase_data = (item_id, purchased_quantity, purchase_date, total_cost)
        cursor.execute(purchase_query, purchase_data)
        connection.commit()

        return total_cost
    except Error as e:
        print("Error while executing query:", e)
        return None
    finally:
        if cursor:
            cursor.close()
            close_database_connection(connection)
