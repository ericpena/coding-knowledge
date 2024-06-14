# TODO: Incude some error handling like if the ISBN number or member id doesn't exist
# TODO: Include transaction logic as well in the Library class to populate transaction DataFrame


import pandas as pd
from abc import ABC, abstractmethod

class Manage(ABC):

    @abstractmethod
    def borrow_book(self):
        pass

    @abstractmethod
    def return_book(self):
        pass

class Book(Manage):
    
    def __init__(self, isbn, title, authors, genre):
        self.isbn = isbn
        self.title = title
        self.authors = authors
        self.genre = genre
        self.__available = True
    
    def borrow_book(self):
        self.__available = False
    
    def return_book(self):
        self.__available = True

    def is_available(self) -> bool:
        return self.__available
    
class Member(Manage):

    def __init__(self, ID, name):
        self.id = ID
        self.name = name
        self.books = {} # :: list of book obejcts
    
    def borrow_book(self, book):
        book.borrow_book()
        self.books[book.isbn] = book

    def return_book(self, book):
        book.return_book()
        self.books.pop(book.isbn)

class Library:
    # :: we could add more attributes to differentiate library from one another
    def __init__(self):
        self.members = {}
        self.books = {}
        self.transactions = pd.DataFrame([])

    def add_book(self, book):
        self.books[book.isbn] = book
        print(f'Library added {book.title}')
    
    def remove_book(self, book):
        self.books.pop(book.isbn)
        print(f'Library removed {book.title}')

    def add_member(self, member):
        self.members[member.id] = member
        print(f'Library added member: {member.name}')
    
    def remove_member(self, member):
        self.members.pop(member.id)
        print(f'Library removed member: {member.name}')
    
    def available_books(self):
        # :: if there's time we can improve what output looks like
        print([book.title for isbn, book in self.books.items() if book.is_available()])

        available_df = pd.DataFrame(columns=(['isbn', 'name']))
        for isbn, book in self.books.items():
            if book.is_available():
                row = pd.DataFrame({'isbn':[book.isbn], 'name':[book.title]})
                available_df = pd.concat([available_df, row], axis=0, ignore_index=True)

        print(available_df)


def main():
    book1 = Book(123, 'fun_book', 'eric', 'amazing')
    book2 = Book(124, 'math_book', 'eric', 'amazing')
    book3 = Book(125, 'weird_book', 'eric', 'amazing')
    book4 = Book(126, 'funny_book', 'eric', 'amazing')
    book5 = Book(127, 'horror_book', 'eric', 'amazing')
    book6 = Book(128, 'self_improvement_book', 'eric', 'amazing')

    books = [book1, book2, book3, book4, book5, book6]

    member1 = Member(1, 'ericpena')
    library = Library()

    for b in books:
        library.add_book(b)

    library.add_member(member1)
    member1.borrow_book(book1)
    library.available_books()

    member1.borrow_book(book3)
    library.available_books()

    print(book1.is_available())
    member1.return_book(book1)
    print('book1 was returned.')
    print(book1.is_available())
    library.available_books()

if __name__ == '__main__':
    main()