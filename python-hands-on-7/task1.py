"""

LEARNING OBJECTIVES:
- Practice CRUD operations with REST APIs
- Implement filtering and searching
- Handle query parameters for sorting and pagination
- Generate summaries and reports
- Work with enumerations and validation

PROJECT OVERVIEW:
Build a REST API to manage a library of books with categories, authors, and reporting features.

INSTRUCTIONS:
Complete the TODO sections below to build a fully functional Book Library AP
Note: Containerize your App
"""

""" Model"""
from enum import Enum
from pydantic import BaseModel
from datetime import date
from typing import List, Optional, Dict

class BookCategory(str, Enum):
    """Enum for book categories"""
    FICTION = "fiction"
    NONFICTION = "nonfiction"
    SCIENCE = "science"
    HISTORY = "history"
    BIOGRAPHY = "biography"
    TECHNOLOGY = "technology"
    OTHER = "other"

class BookCreate(BaseModel):
    title: str
    author: str
    category: BookCategory
    published_date: date

class Book(BookCreate):
    id: int

class AuthorSummary(BaseModel):
    author: str
    book_count: int


class CategorySummary(BaseModel):
    category: str
    book_count: int


""" Databasemodel"""

from typing import List, Optional

class Database:
    """In-memory database template for books"""

    def __init__(self):
        self._books: List[Book] = []
        self._current_id = 1

    def generate_id(self) -> int:
        """Generate next book ID"""
        # TODO: Implement ID generation
        pass

    def add_book(self, book: BookCreate) -> Book:
        """Add a new book to the database"""
        # TODO: Implement adding a book
        pass

    def get_all_books(self) -> List[Book]:
        """Return all books"""
        # TODO: Implement retrieving all books
        pass

    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        """Find a book by ID"""
        # TODO: Implement lookup by ID
        pass

    def update_book(self, book_id: int, updates: dict) -> Optional[Book]:
        """Update book details by ID"""
        # TODO: Implement update
        pass

    def delete_book(self, book_id: int) -> bool:
        """Delete a book by ID"""
        # TODO: Implement delete
        pass

    def get_books_by_category(self, category: BookCategory) -> List[Book]:
        """Retrieve all books in a given category"""
        # TODO: Implement category filter
        pass

    def get_author_summary(self) -> List[AuthorSummary]:
        """Return count of books per author"""
        # TODO: Implement author summary
        pass

    def get_category_summary(self) -> List[CategorySummary]:
        """Return count of books per category"""
        # TODO: Implement category summary
        pass

"""
API ENDPOINT
"""

from fastapi import FastAPI, HTTPException, status
from typing import List, Optional

app = FastAPI(title="Book Library API")

db = Database()  # in-memory database instance

@app.post("/books")
def create_book(book: BookCreate):
    """Add a new book"""
    # TODO: Call db.add_book and return the new book
    pass

@app.get("/books")
def list_books(category: Optional[BookCategory] = None) -> List[Book]:
    """List all books or filter by category"""
    # TODO: Return db.get_all_books or db.get_books_by_category
    pass

@app.get("/books/{book_id}")
def get_book(book_id: int):
    """Retrieve a book by ID"""
    # TODO: Return db.get_book_by_id or raise 404
    pass

@app.put("/books/{book_id}")
def update_book(book_id: int, updates: BookCreate):
    """Update a book by ID"""
    # TODO: Call db.update_book and return updated book
    pass

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    """Delete a book by ID"""
    # TODO: Call db.delete_book or raise 404
    pass

@app.get("/summary/authors")
def author_summary():
    """Return summary of books per author"""
    # TODO: Call db.get_author_summary
    pass

@app.get("/summary/categories")
def category_summary():
    """Return summary of books per category"""
    # TODO: Call db.get_category_summary
    pass
