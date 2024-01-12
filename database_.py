import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        db_config = {
            "host": "localhost",
            "database": "employee",
            "user": "root",
            "password": "",
        }

        conn = mysql.connector.connect(**db_config)

        if conn.is_connected():
            print("Successfully connected to the database")
            return conn

    except Error as e:
        print("Error connecting to the database:", e)
        return None

if __name__ == "__main__":
    connection = get_db_connection()
