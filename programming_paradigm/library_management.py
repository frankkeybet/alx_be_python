class Book:
    """
    Represents a single book in the library.
    Contains public attributes title and author,
    and a private attribute _is_checked_out to track availability.
    """

    def __init__(self, title, author):
        # Public attributes
        self.title = title
        self.author = author

        # Private attribute: True if the book is currently checked out
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available again."""
        self._is_checked_out = False

    def is_available(self):
        """
        Check if the book is available (not checked out).
        Returns True if available, False otherwise.
        """
        return not self._is_checked_out


class Library:
    """
    Represents a library that stores and manages Book objects.
    Uses a private list _books to keep all books.
    """

    def __init__(self):
        # Private list storing all Book instances
        self._books = []

    def add_book(self, book):
        """
        Add a Book instance to the library's collection.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book by its title.
        Only works if the book exists AND is available.
        Returns True if successful, False otherwise.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        """
        Return a book by its title.
        Only works if the book exists AND is currently checked out.
        Returns True if successful, False otherwise.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """
        Print the title and author of all available books.
        Matches the exact output format expected in main.py.
        """
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
            
from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()

