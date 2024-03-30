from getpass import getpass
from mysql.connector import Error
from database import create_connection
import models

#register user function
def register_user():
   connection = create_connection()
   username = input("Enter username: ")
   password = getpass("Enter password: ")
   try:
       cursor = connection.cursor()
       cursor.execute(models.REGISTER_USER, (username, password))
       connection.commit()
       print("User registered successfully")
   except Error as e:
       print(e)
   finally:
       connection.close()
def login_user():
   connection = create_connection()
   username = input("Enter username: ")
   password = getpass("Enter password: ")
   try:
       cursor = connection.cursor()
       cursor.execute(models.LOGIN_USER, (username, password))
       result = cursor.fetchone()
       if result:
           print("Login successful")
           return result[0]  # Return the user_id
       else:
           print("Login failed")
           return None
   except Error as e:
       print(e)
  finally:
       connection.close()

