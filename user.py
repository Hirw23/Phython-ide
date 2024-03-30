def register_user():
   connection = create_connection()
   username = input("Enter username: ")
   password = getpass("Enter password: ")
   try:
       cursor = connection.cursor()
       cursor.execute(models.REGISTER_USER, (username, password))
       connection.commit()
       print("User registered successfully.")
   except Error as e:
       print(e)
   finally:
       connection.close()