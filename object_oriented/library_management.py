# create a library script where a library has multiple books

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False

    def __str__(self):
        status = "Checked Out" if self.is_checked_out else "Available"
        return f"'{self.title}' by {self.author} [{status}]"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def checkout_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.is_checked_out:
                book.is_checked_out = True
                print(f"You have checked out: {book.title}")
                return
        print("Book not found or already checked out.")

    def list_books(self):
        print("\nLibrary Catalog:")
        for book in self.books:
            print(book)

if __name__ == "__main__":
    my_lib = Library()
    my_lib.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "12345"))
    my_lib.add_book(Book("1984", "George Orwell", "67890"))

    my_lib.list_books()
    my_lib.checkout_book("12345")
    my_lib.list_books()