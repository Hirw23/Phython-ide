from mysql.connector import connect, Error

def create_connection():
    try:
        return connect(
            host="localhost",
            user="root",
            password="123@nshimiye",
            database="shopDB",
        )
    except Error as e:
        print(e)
