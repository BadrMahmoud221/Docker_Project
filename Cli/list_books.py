import requests

BASE_URL = "https://dockerproject-production-ced3.up.railway.app"

def list_books():
    response = requests.get(f"{BASE_URL}/books")

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