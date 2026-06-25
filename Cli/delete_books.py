import requests

BASE_URL = "https://dockerproject-production-ced3.up.railway.app"

def delete_book(book_id):
    response = requests.delete(f"{BASE_URL}/{book_id}")

    if response.status_code == 204:
        print("🗑️ Book deleted successfully")
    else:
        print(response.text)