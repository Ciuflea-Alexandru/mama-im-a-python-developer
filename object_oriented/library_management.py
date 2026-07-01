# create a library script where a library has multiple books

class Book:
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.is_checked_out = False

    def check_out(self):
        """Logic specific to changing the book's internal state."""
        if self.is_checked_out:
            return False, "Book is already checked out."
        self.is_checked_out = True
        return True, "Book checked out successfully."

    def __repr__(self):
        """Provides a helpful string representation for debugging."""
        return f"Book(title='{self.title}', isbn='{self.isbn}')"

if __name__ == "__main__":
    my_book = Book("The Hobbit", "J.R.R. Tolkien", "978-0547928227", 1937)
    
    success, message = my_book.check_out()
    print(f"Status: {message}")
    print(f"Current Book Object: {my_book}")