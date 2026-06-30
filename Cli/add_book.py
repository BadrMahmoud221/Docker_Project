import requests

BASE_URL = "https://finalproject-production-2bdb.up.railway.app/books"

def add_book(title, author , isbn, published_year, genre, available = True):
    response = requests.post(BASE_URL,
        json={"title": title,"author": author,"isbn": isbn,"published_year": published_year,"genre": genre,"available": available})

    if response.ok:
        print("✅ Book added successfully")
    else:
        print("❌ Failed to add book")