class Book:
    def __init__(self, name, author, quantity=1):
        self.name = name
        self.author = author
        self.quantity = quantity
        self.borrowed = False
        self.username = '' # Initially we don't have any user
    def borrow(self, username):
        self.borrowed = True
        self.username = username
    def return_back(self, username):
        self.borrowed = False
        self.username = ''
    def display(self):
        print(self.name, self.author, self.quantity)
