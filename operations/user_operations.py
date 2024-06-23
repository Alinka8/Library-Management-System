from db_connection import connect_db
from models import User
from mysql.connector import Error

def add_user(user):
    try:
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name, library_id) VALUES (%s, %s)", (user.name, user.library_id))
            conn.commit()
            print("User added successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

def view_user_details(user_id):
    try:
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            row = cursor.fetchone()
            print(row)
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

def display_all_users():
    try:
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()
