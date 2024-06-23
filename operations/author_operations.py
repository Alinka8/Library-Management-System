from db_connection import connect_db
from models import Author
from mysql.connector import Error

def add_author(author):
    try:
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO authors (name, biography) VALUES (%s, %s)", (author.name, author.biography))
            conn.commit()
            print("Author added successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

def view_author_details(author_id):
    try:
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM authors WHERE id = %s", (author_id,))
            row = cursor.fetchone()
            print(row)
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

def display_all_authors():
    try:
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM authors")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()
