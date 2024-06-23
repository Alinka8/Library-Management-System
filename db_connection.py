import mysql.connector
from mysql.connector import Error

def connect_db():
    try:
        conn = mysql.connector.connect(
            host='LibraryManagementSystem.db',
            user='root',
            password='2001Alina',
            database='LibraryDB'
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error: {e}")
        return None