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
        print("-" * 50)
        print(f" ID: {book['id']}")
        print(f" Title          : {book['title']}")
        print(f" Author         : {book['author']}")
        print(f" ISBN           : {book['isbn']}")
        print(f" Published Year : {book['published_year']}")
        print(f" Genre          : {book['genre']}")
        print(f" Available      : {book['available']}")
        print("-" * 50)