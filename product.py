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
def view_products():
  connection = create_connection()
  try:
      cursor = connection.cursor()
      cursor.execute(models.VIEW_PRODUCTS)
      result = cursor.fetchall()
      if result:
          # Print table header
          print(f"{'ID':<5} {'Name':<20} {'Description':<30} {'Price':<10} {'Stock':<5}")
          print("-" * 75)  # Print a separator line
 
          # Iterate over each product and print each one in a formatted row
          for row in result:
              product_id, name, description, price, stock = row
              print(f"{product_id:<5} {name:<20} {description[:28]:<30} ${price:<10} {stock:<5}")
              print("-" * 75)
      else:
          print("No products available.")
  except Error as e:
      print(e)
  finally:
      connection.close()
