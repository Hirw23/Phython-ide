from mysql.connector import Error
from getpass import getpass
from database import create_connection
import models

def add_product(user_id):
    connection = create_connection()
    product_name = input("Enter product name: ")
    description = input("Enter product description: ")
    price = input("Enter product price: ")
    try:
        cursor = connection.cursor()
        cursor.execute(models.ADD_PRODUCT, (product_name, description, price, user_id))
        connection.commit()
        print("Product added successfully.")
    except Error as e:
        print(e)
    finally:
        connection.close()

