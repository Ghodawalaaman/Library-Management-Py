from book import *

class Library:
    def __init__(self):
        self.books = []
    def add(self, new_book):
        for book in self.books:
            if book.name == new_book.name and book.author == new_book.author:
                book.quantity += 1
                return
        self.books.append(new_book)
    def remove(self, book_name, book_author):
        for book in self.books:
            if book.name == book_name and book.author == book_author:
                if book.quantity == 1:
                    self.books.remove(book)
                else:
                    book.quantity -= 1
#        self.books.pop(self.books.find(key=lambda book: book.name == book_name and book.author == book_author))

# Testing the class
l = Library()
l.add(Book("book1", "kaif"))
print(l.books[0].name)
