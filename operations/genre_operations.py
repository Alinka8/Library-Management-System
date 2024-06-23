from db_connection import connect_db
from models import Genre
from mysql.connector import Error

def add_genre(genre):
    try:
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO genres (name, description, category) VALUES (%s, %s, %s)", (genre.name, genre.description, genre.category))
            conn.commit()
            print("Genre added successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

def view_genre_details(genre_id):
    try:
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM genres WHERE id = %s", (genre_id,))
            row = cursor.fetchone()
            print(row)
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

def display_all_genres():
    try:
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM genres")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()
