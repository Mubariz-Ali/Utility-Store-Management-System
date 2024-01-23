from utils.database import connect_to_database, close_database_connection
from mysql.connector import Error


def profit_reports(report_start_date, report_end_date):
    connection = connect_to_database()
    if not connection:
        return None, None, None

    try:
        cursor = connection.cursor(dictionary=True)

        sale_query = f"SELECT DATE_FORMAT(sale_date, '%%Y-%%m-%%d') AS date, SUM(quantity_sold) AS " \
                     f"quantity_sold, SUM(total_price) AS total_sales FROM sale WHERE sale_date BETWEEN %s AND %s " \
                     "GROUP BY date"
        cursor.execute(sale_query, (report_start_date, report_end_date))
        sales_report = cursor.fetchall()

        purchase_query = f"SELECT DATE_FORMAT(purchase_date, '%%Y-%%m-%%d') AS date, SUM(quantity_purchased) AS " \
                         "quantity_purchased, SUM(total_price) AS total_purchased FROM purchase WHERE " \
                         f"purchase_date BETWEEN %s AND %s GROUP BY date"
        cursor.execute(purchase_query, (report_start_date, report_end_date))
        purchase_report = cursor.fetchall()

        profit_report = []
        for sales_row in sales_report:
            date = sales_row['date']
            quantity_sales = sales_row['quantity_sold']
            total_sales = sales_row['total_sales']

            purchase_row = next((row for row in purchase_report if row['date'] == date), None)

            if purchase_row:
                total_purchase = purchase_row['total_purchased']
                quantity_purchase = purchase_row['quantity_purchased']
                profit = total_sales - total_purchase
                profit_report.append((date, profit, quantity_sales, quantity_purchase))

        return sales_report, purchase_report, profit_report

    except Error as e:
        print("Error while connecting to MySQL:", e)
        return None, None, None

    finally:
        if cursor:
            cursor.close()
            close_database_connection(connection)
