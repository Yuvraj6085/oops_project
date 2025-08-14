class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False  

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' added to the library.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"'{book.title}' removed from the library.")
                return
        print("Book not found.")

    def search_book(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if found_books:
            for b in found_books:
                print(b)
        else:
            print("No matching books found.")

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"You borrowed '{book.title}'.")
                else:
                    print("Book is already borrowed.")
                return
        print("Book not found.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"You returned '{book.title}'.")
                else:
                    print("This book was not borrowed.")
                return
        print("Book not found.")

    def display_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            for book in self.books:
                print(book)
library = Library()
book1 = Book("Python", "Amit", "123")
book2 = Book("java", "vint", "456")
library.add_book(book1)
library.add_book(book2)


library.display_books()


library.search_book("1984")

library.borrow_book("123")
library.display_books()
library.return_book("123")


library.remove_book("456")
library.display_books()
