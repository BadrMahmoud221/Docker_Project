import argparse

from add_book import add_book
from list_books import list_books
from delete_books import delete_book


parser = argparse.ArgumentParser(add_help=False)

subparsers = parser.add_subparsers(dest="command")

# Add
add_parser = subparsers.add_parser("add")
add_parser.add_argument("title")
add_parser.add_argument("author")
add_parser.add_argument("isbn", default=None)
add_parser.add_argument("published_year", type=int, default=None)
add_parser.add_argument("genre", default=None)
add_parser.add_argument("available", type=bool, default=True)

# List
subparsers.add_parser("list")

# Delete
delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("id", type=int)

args = parser.parse_args()


if not args.command:
    print(r"""
📚 Welcome to Book CLI

1. Add Book
    python Cli\cli.py add "Title" "Author" "ISBN" "Published Year" "Genre" "Available"
2. List Books
   python Cli\cli.py list

3. Delete Book
   python Cli\cli.py delete "Book ID"
""")
    exit()


if args.command == "add":
    add_book(args.title,args.author,args.isbn,args.published_year,args.genre,args.available)
elif args.command == "list":
    list_books()

elif args.command == "delete":
    delete_book(args.id)