"""
library_system.py

Problem Statement:
------------------
Design and implement a mini Library Management System using OOP principles:
- Classes and Objects
- Inheritance
- Polymorphism

Requirements:
1. Create a base class `Book` with attributes:
   - title
   - author
   - publication year
   - availability status (borrowed/available)

2. Create two subclasses:
   - `EBook` (inherits from Book, adds file size in MB)
   - `PrintedBook` (inherits from Book, adds number of pages)

3. Demonstrate polymorphism:
   - Implement a `get_details()` method that behaves differently
     for EBook and PrintedBook.

4. Create a `Library` class that can:
   - Add books (both EBook and PrintedBook)
   - Search books by title (case-insensitive)
   - Borrow and return books
   - Display all books with availability status

5. Write a demo program that:
   - Creates both EBook and PrintedBook objects
   - Adds them to a Library
   - Displays available books
   - Allows borrowing and returning of books
   - Shows the effect of these operations on availability status
"""

from typing import List, Optional


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def borrow(self) -> bool:
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self) -> None:
        self.is_available = True

    def get_details(self) -> str:
        raise NotImplementedError("Subclass must implement this method")


class EBook(Book):
    def __init__(self, title: str, author: str, year: int, file_size: float):
        super().__init__(title,author,year)
        self.file_size = file_size

    def get_details(self) -> str:
        return f"[EBook] {self.title} by {self.author}, {self.year}, file size : {self.file_size}MB"


class PrintedBook(Book):
    def __init__(self, title: str, author: str, year: int, pages: int):
        super().__init__(title,author,year)
        self.pages = pages

    def get_details(self) -> str:
        return f"[PrintBook] {self.title} by {self.author}, {self.year}, Pages : {self.pages}"


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def search_by_title(self, title: str) -> Optional[Book]:
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def display_books(self) -> None:
        for book in self.books:
            status = "Available" if book.is_available else "Borrowed"
            print(f"{book.get_details()} - Status: {status}")



if __name__ == "__main__":
    # Demo usage
    lib = Library()

    ebook = EBook("Python 101", "John Doe", 2020, 5.2)
    printed = PrintedBook("Clean COde","Robert C. Martin", 2008, 463)

    lib.add_book(ebook)
    lib.add_book(printed)

    lib.display_books()

    book = lib.search_by_title("Clean COde")
    if book and book.borrow():
        print(f"\nBorrowed : {book.title}")
    else:
        print("\nBook not available")

    lib.display_books()