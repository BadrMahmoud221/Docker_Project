import requests

BASE_URL = "https://finalproject-production-2bdb.up.railway.app/books"

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