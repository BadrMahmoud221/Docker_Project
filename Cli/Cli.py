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
   python Cli\cli.py add "Book Title" "Author"

2. List Books
   python Cli\cli.py list

3. Delete Book
   python Cli\cli.py delete "Book ID"
""")
    exit()


if args.command == "add":
    add_book(args.title, args.author)

elif args.command == "list":
    list_books()

elif args.command == "delete":
    delete_book(args.id)