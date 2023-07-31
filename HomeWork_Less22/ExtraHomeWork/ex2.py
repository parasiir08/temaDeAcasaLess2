class Book:

    def __init__(self, titlu, autor, id_carte, disponibila=True):
        self.titlu = titlu
        self.autor = autor
        self.__id_carte = id_carte
        self.__disponibila = disponibila

    def get_title(self):
        return self.titlu

    def get_author(self):
        return self.autor

    def get_book_id(self):
        return self.__id_carte

    def is_book_available(self):
        return self.__disponibila

    def borrow_book(self):
        if self.__disponibila:
            self.__disponibila = False
            return True
        else:
            return False

    def return_book(self):
        if not self.__disponibila:
            self.__disponibila = True
            return True
        else:
            return False

class Library:

    def __init__(self, nume, locatie):
        self.nume = nume
        self.locatie = locatie
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, book):
        if book in self.__books:
            self.__books.remove(book)

    def search_book(self, title):
        for book in self.__books:
            if book.get_title().lower() == title.lower():
                return book
        return None

    def list_available_books(self):
        available_books = [book for book in self.__books if book.is_book_available()]
        return available_books

def test_book_functionality():
    book1 = Book("Book 1", "Author 1", "ID001")
    book2 = Book("Book 2", "Author 2", "ID002")

    # Test book availability
    assert book1.is_book_available() is True
    assert book2.is_book_available() is True

    # Test borrow_book
    assert book1.borrow_book() is True
    assert book1.is_book_available() is False

    # Try to borrow the same book again (should return False as it's already borrowed)
    assert book1.borrow_book() is False
    assert book1.is_book_available() is False

    # Test return_book
    assert book1.return_book() is True
    assert book1.is_book_available() is True

    # Try to return the book again (should return False as it's already returned)
    assert book1.return_book() is False
    assert book1.is_book_available() is True

def test_library_functionality():
    library = Library("My Library", "City Center")
    book1 = Book("Book 1", "Author 1", "ID001")
    book2 = Book("Book 2", "Author 2", "ID002")
    book3 = Book("Book 3", "Author 3", "ID003")

    # Test adding books to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Test searching for a book
    searched_book = library.search_book("Book 2")
    assert searched_book is book2

    # Test borrowing and returning books
    assert searched_book.borrow_book() is True
    assert searched_book.is_book_available() is False

    assert searched_book.return_book() is True
    assert searched_book.is_book_available() is True

    # Test listing available books
    available_books = library.list_available_books()
    assert len(available_books) == 3  # All books are available at this point

    # Borrow a book and test the list again
    library.search_book("Book 1").borrow_book()
    available_books = library.list_available_books()
    assert len(available_books) == 2

    print("All tests passed successfully!")

# Run the tests
test_book_functionality()
test_library_functionality()
