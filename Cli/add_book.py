import requests

BASE_URL = "http://127.0.0.1:8000/books"

def add_book(title, author):
    response = requests.post(
        BASE_URL,
        json={
            "title": title,
            "author": author
        }
    )

    if response.ok:
        print("✅ Book added successfully")
    else:
        print("❌ Failed to add book")