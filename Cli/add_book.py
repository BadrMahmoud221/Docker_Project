import requests

BASE_URL = "https://finalproject-production-2bdb.up.railway.app/books"

def add_book(title, author):
    response = requests.post(BASE_URL,
        json={
            "title": title,
            "author": author
        }
    )

    if response.ok:
        print("✅ Book added successfully")
    else:
        print("❌ Failed to add book")