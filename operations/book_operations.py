from db_connection import connect_db
from models import Book
from mysql.connector import Error

def add_book(book):
    try:
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO books (title, author_id, genre_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s, %s)",
                           (book.title, book.author_id, book.genre_id, book.isbn, book.publication_date, book.availability))
            conn.commit()
            print("Book added successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

def borrow_book(user_id, book_id):
    try:
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, CURDATE())", (user_id, book_id))
            cursor.execute("UPDATE books SET availability = FALSE WHERE id = %s", (book_id,))
            conn.commit()
            print("Book borrowed successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

def return_book(book_id):
    try:
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE borrowed_books SET return_date = CURDATE() WHERE book_id = %s AND return_date IS NULL", (book_id,))
            cursor.execute("UPDATE books SET availability = TRUE WHERE id = %s", (book_id,))
            conn.commit()
            print("Book returned successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

def search_book_by_title(title):
    try:
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books WHERE title LIKE %s", ('%' + title + '%',))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

def display_all_books():
    try:
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()
