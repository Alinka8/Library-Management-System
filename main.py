from operations.book_operations import *
from operations.user_operations import *
from operations.author_operations import *
from operations.genre_operations import *
from models import Book
from models import User
from models import Author
from models import Genre

def main_menu():
    while True:
        print("Welcome to the Library Management System with Database Integration!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Genre Operations")
        print("5. Quit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            book_operations()
        elif choice == '2':
            user_operations()
        elif choice == '3':
            author_operations()
        elif choice == '4':
            genre_operations()
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

def book_operations():
    while True:
        print("Book Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to main menu")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author_id = int(input("Enter author ID: "))
            genre_id = int(input("Enter genre ID: "))
            isbn = input("Enter ISBN: ")
            publication_date = input("Enter publication date (YYYY-MM-DD): ")
            book = Book(title, author_id, genre_id, isbn, publication_date)
            add_book(book)
        elif choice == '2':
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))
            borrow_book(user_id, book_id)
        elif choice == '3':
            book_id = int(input("Enter book ID: "))
            return_book(book_id)
        elif choice == '4':
            title = input("Enter book title to search: ")
            search_book_by_title(title)
        elif choice == '5':
            display_all_books()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def user_operations():
    while True:
        print("User Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to main menu")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter user name: ")
            library_id = input("Enter library ID: ")
            user = User(name, library_id)
            add_user(user)
        elif choice == '2':
            user_id = int(input("Enter user ID: "))
            view_user_details(user_id)
        elif choice == '3':
            display_all_users()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def author_operations():
    while True:
        print("Author Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Back to main menu")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter author name: ")
            biography = input("Enter biography: ")
            author = Author(name, biography)
            add_author(author)
        elif choice == '2':
            author_id = int(input("Enter author ID: "))
            view_author_details(author_id)
        elif choice == '3':
            display_all_authors()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def genre_operations():
    while True:
        print("Genre Operations:")
        print("1. Add a new genre")
        print("2. View genre details")
        print("3. Display all genres")
        print("4. Back to main menu")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter genre name: ")
            description = input("Enter description: ")
            category = input("Enter category: ")
            genre = Genre(name, description, category)
            add_genre(genre)
        elif choice == '2':
            genre_id = int(input("Enter genre ID: "))
            view_genre_details(genre_id)
        elif choice == '3':
            display_all_genres()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()