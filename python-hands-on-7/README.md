# 📚 BOOK LIBRARY API — HANDS-ON PROJECT

A beginner-friendly REST API project built with **FastAPI** to manage a digital book library.  
This project helps you practice API design, request handling, data models, query filtering, sorting, and Docker deployment.

---

## 🎯 LEARNING OBJECTIVES

By completing this project, you will learn to:

- Work with **FastAPI** to build REST APIs  
- Design and validate **Pydantic models**  
- Implement **CRUD (Create, Read, Update, Delete)** operations  
- Use **query parameters** and **path parameters**  
- Add **filtering**, **sorting**, and **pagination**  
- Generate **summaries and reports** (aggregations)  
- Run your API inside a **Docker container**  

## 📦 book-library-api
- ┣ 📜 main.py # FastAPI app (TODO sections to complete)
- ┣ 📜 requirements.txt # Dependencies list
- ┣ 📜 Dockerfile # Docker instructions
- ┣ 📜 README.md # This file
  
## 🧠 PROJECT OVERVIEW

You are building a small REST API for managing a book library.  
Users should be able to:

- Add new books  
- Get all books (with filtering and sorting)  
- Retrieve a book by ID  
- Update or delete a book  
- View reports, summaries, and author statistics  

All data is stored in a **simple in-memory database** (`Database` class), so you can focus on building API logic rather than setup.

---

## 🧩 ENDPOINTS OVERVIEW
Method	Endpoint	Description
- POST	/books	Add a new book
- GET	/books	List all books (supports filters and sorting)
- GET	/books/{book_id}	Retrieve a book by ID
- PUT	/books/{book_id}	Update a book
- DELETE	/books/{book_id}	Delete a book
- GET	/summary/authors	Get number of books per author
- GET	/summary/categories	Get summary by category
GET	/stats	View overall library statistics


## CHALLENGE QUESTIONS / TODOs

Complete all # TODO: sections in the code to finish your API.

- Implement CRUD operations inside Database class.

- Add filtering by category, author, and sorting by title or date.
- Add pagination with query parameters (?skip=0&limit=10).
- Implement /summary/authors and /summary/categories endpoints.
- Implement /stats endpoint for total counts, averages, highest and lowest.
- (Bonus) Add a /search endpoint that allows searching by keyword in title or description.
