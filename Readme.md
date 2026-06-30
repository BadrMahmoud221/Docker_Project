# 📚 Book Manager API

## Overview

The **Book Manager API** is a RESTful application built with **FastAPI** that allows users to manage a collection of books. It includes a **Python CLI** client that communicates with the API over HTTP.

Features:
- ➕ Add books
- 📚 List all books
- 🗑️ Delete books
- 📝 Store title, author, ISBN, published year, genre, and availability

---

## Run the API

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
uvicorn app.main:app --reload
```

API:
```
http://127.0.0.1:8000
```

Swagger Docs:
```
http://127.0.0.1:8000/docs
```

---

## CLI Usage

Run:

```bash
python Cli\cli.py
```

Available commands:

```bash
# Add a book
python Cli\cli.py add "<Title>" "<Author>" "<ISBN>" <Published_Year> "<Genre>" <Available>

# List all books
python Cli\cli.py list

# Delete a book
python Cli\cli.py delete <Book_ID>
```

Example:

```bash
python Cli\cli.py add "Python Basics" "Badr Mahmoud" "9780135957059" 2025 "Programming" True
```