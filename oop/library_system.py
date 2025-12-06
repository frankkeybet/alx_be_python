class Book:
    """Base class representing a generic book."""
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an ebook (adds file_size)."""
    def __init__(self, title: str, author: str, file_size: int):
        # initialize base attributes
        super().__init__(title, author)
        # initialize ebook-specific attribute (in KB)
        self.file_size = file_size

    def __str__(self) -> str:
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a print book (adds page_count)."""
    def __init__(self, title: str, author: str, page_count: int):
        # initialize base attributes
        super().__init__(title, author)
        # initialize print-book-specific attribute
        self.page_count = page_count

    def __str__(self) -> str:
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Composition: Library manages a collection of Book (or derived) instances."""
    def __init__(self):
        self.books = []  # list to hold Book / EBook / PrintBook instances

    def add_book(self, book):
        # safety: ensure only Book instances (or subclasses) are added
        if not isinstance(book, Book):
            raise TypeError("add_book expects an instance of Book or a subclass of Book")
        self.books.append(book)

    def list_books(self):
        # print details of each stored book
        if not self.books:
            print("The library is empty.")
            return

        for book in self.books:
            print(book)  # relies on each class's __str__ implementation


# The testing code (same behavior as your provided main.py)
def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()


if __name__ == "__main__":
    main()
