from enum import Enum
from pydantic import BaseModel
from datetime import date
from typing import List, Optional, Dict
from fastapi import FastAPI, HTTPException, status

"""
LEARNING OBJECTIVES:
- Practice CRUD operations with REST APIs
- Implement filtering and searching
- Handle query parameters for sorting and pagination
- Generate summaries and reports
- Work with enumerations and validation

PROJECT OVERVIEW:
Build a REST API to manage a library of books with categories, authors, and reporting features.
"""

# -------------------------------
# MODEL
# -------------------------------

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


# -------------------------------
# DATABASE SIMULATION
# -------------------------------

class Database:
    """In-memory database template for books"""

    def __init__(self):
        self._books: List[Book] = []
        self._next_id = 1  # fixed variable name

    def generate_id(self) -> int:
        """Generate next book ID"""
        next_book_id = self._next_id
        self._next_id += 1
        return next_book_id

    def add_book(self, book: BookCreate) -> Book:
        """Add a new book to the database"""
        new_book = Book(id=self.generate_id(), **book.dict())
        self._books.append(new_book)
        return new_book

    def get_all_books(self) -> List[Book]:
        """Return all books"""
        return list(self._books)

    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        """Find a book by ID"""
        for book in self._books:
            if book.id == book_id:
                return book
        return None

    def update_book(self, book_id: int, updates: dict) -> Optional[Book]:
        """Update book details by ID"""
        for book in self._books:
            if book.id == book_id:
                book.title = updates.get("title", book.title)
                book.author = updates.get("author", book.author)
                book.category = updates.get("category", book.category)
                book.published_date = updates.get("published_date", book.published_date)
                return book
        return None

    def delete_book(self, book_id: int) -> bool:
        """Delete a book by ID"""
        for book in self._books:
            if book.id == book_id:
                self._books.remove(book)
                return True
        return False

    def get_books_by_category(self, category: BookCategory) -> List[Book]:
        """Retrieve all books in a given category"""
        return [book for book in self._books if book.category == category]

    def get_author_summary(self) -> List[AuthorSummary]:
        """Return count of books per author"""
        author_counts: Dict[str, int] = {}
        for book in self._books:
            author_counts[book.author] = author_counts.get(book.author, 0) + 1
        return [AuthorSummary(author=a, book_count=c) for a, c in author_counts.items()]

    def get_category_summary(self) -> List[CategorySummary]:
        """Return count of books per category"""
        category_counts: Dict[str, int] = {}
        for book in self._books:
            category_counts[book.category] = category_counts.get(book.category, 0) + 1
        return [CategorySummary(category=k, book_count=v) for k, v in category_counts.items()]


# -------------------------------
# API ENDPOINTS
# -------------------------------

app = FastAPI(title="Book Library API")
db = Database()  # in-memory database instance


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    """Add a new book"""
    if not all([book.title, book.author, book.category, book.published_date]):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="All fields are required")
    new_book = db.add_book(book)
    return new_book


@app.get("/books", response_model=List[Book])
def list_books(category: Optional[BookCategory] = None):
    """List all books or filter by category"""
    if category:
        return db.get_books_by_category(category)
    return db.get_all_books()


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    """Retrieve a book by ID"""
    book = db.get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updates: BookCreate):
    """Update a book by ID"""
    updated_book = db.update_book(book_id, updates.dict())
    if not updated_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return updated_book


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    """Delete a book by ID"""
    deleted = db.delete_book(book_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return None


@app.get("/summary/authors", response_model=List[AuthorSummary])
def author_summary():
    """Return summary of books per author"""
    return db.get_author_summary()


@app.get("/summary/categories", response_model=List[CategorySummary])
def category_summary():
    """Return summary of books per category"""
    return db.get_category_summary()
