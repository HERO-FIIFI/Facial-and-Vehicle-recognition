import datetime
import mysql.connector
from mysql.connector import Error
from database_ import get_db_connection

# Establish database connection
connection = get_db_connection()

# Insert random details workers
workers = [
    ("John", "Doe", "EMP001", datetime.date(1990, 1, 1), "john@example.com", "Ghananian","GHA342567","+1234567890", "123 Main St"),
    ("Jane", "Smith", "EMP002", datetime.date(1991, 2, 2), "jane@example.com","Ghananian", "GHA342567","+2345678901", "456 Elm St"),
    ("Alice", "Johnson", "EMP003", datetime.date(1985, 3, 3), "alice@example.com","Senegalese","SNG342567", "+3456789012", "789 Oak St"),
    ("Bob", "Williams", "EMP004", datetime.date(1980, 4, 4), "bob@example.com","Ghananian","GHA342567", "+4567890123", "567 Pine St"),
    ("Eva", "Anderson", "EMP005", datetime.date(1975, 5, 5), "eva@example.com", "Nigerian","NGN5545666","+5678901234", "101 Cedar St"),
]


def add_employee(conn, emp_id, first_name=None, last_name=None, birth_date=None, email=None,native=None,native_id=None, phone=None, address=None):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO employees (first_name, last_name, emp_id, birth_date, email, native ,native_id ,phone, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (first_name, last_name, emp_id, birth_date, email, phone, address))
        conn.commit()
    except Error as e:
        print("Error adding employee:", e)
for worker in workers:
    add_employee(connection, *worker)



def delete_employee(conn, emp_id):
    try:
        cursor = conn.cursor()
        query = "DELETE FROM employees WHERE emp_id = %s"
        cursor.execute(query, (emp_id,))
        conn.commit()
    except Error as e:
        print("Error deleting employee:", e)
for worker in workers:
    delete_employee(connection, *worker)



def edit_employee(conn, emp_id, first_name=None, last_name=None, birth_date=None, email=None,native=None,native_id=None, phone=None, address=None):
    try:
        cursor = conn.cursor()
        query = "UPDATE employees SET first_name = %s, last_name = %s, birth_date = %s, email = %s,native = %s,native_id = %s, phone = %s, address = %s WHERE emp_id = %s"
        cursor.execute(query, (first_name, last_name, birth_date, email, phone, address, emp_id))
        conn.commit()
    except Error as e:
        print("Error editing employee:", e)
for worker in workers:
    edit_employee(connection, *worker)

