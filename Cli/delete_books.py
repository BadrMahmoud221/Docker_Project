import requests

BASE_URL = "http://127.0.0.1:8000/books"

def delete_book(book_id):
    response = requests.delete(f"{BASE_URL}/{book_id}")

    if response.status_code == 204:
        print("🗑️ Book deleted successfully")
    else:
        print(response.text)