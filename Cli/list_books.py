import requests

BASE_URL = "http://127.0.0.1:8000/books"

def list_books():
    response = requests.get(BASE_URL)

    books = response.json()

    if not books:
        print("📭 No books found")
        return

    print("\n📚 Books:\n")

    for book in books:
        print(
            f"ID: {book['id']} | "
            f"Title: {book['title']} | "
            f"Author: {book['author']}"
        )