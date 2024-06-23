class Book:
    def __init__(self, title, author_id, genre_id, isbn, publication_date, availability=True):
        self.title = title
        self.author_id = author_id
        self.genre_id = genre_id
        self.isbn = isbn
        self.publication_date = publication_date
        self.availability = availability

class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id

class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

class Genre:
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category
