import requests

BASE_URL = "https://dockerproject-production-ced3.up.railway.app"

def add_book(title, author):
    response = requests.post(f"{BASE_URL}/books",
        json={
            "title": title,
            "author": author
        }
    )

    if response.ok:
        print("✅ Book added successfully")
    else:
        print("❌ Failed to add book")