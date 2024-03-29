from mysql.connector import connect, Error

def create_connection():
    try:
        return connect(
            host="localhost",
            user="root",
            password=" ",
            database=" ",
        )
    except Error as e:
        print(e)
