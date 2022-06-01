from pymongo import MongoClient
from requests import delete

cl = MongoClient()
db = cl['lbms']
books = db['books']

def printf():
    for book in books.find():
        print(f"Name: {book['name']}")
        print(f"Author: {book['author']}")
        print(f"Count: {book['count']}")
        print("\n")

def checkout():
    name = input("Enter the name of the book: ")
    for book in books.find({"name": name}):
        if book['count'] > 0:
            books.update_one(book, {"$set": {"count": book['count']-1}})
            print("Book checked out successfully")
        else:
            print("Book not available")

def insert():
    name = input("Enter the name of the book: ")
    author = input("Enter the name of the author: ")
    count = int(input("Enter the number of books: "))
    books.insert_one({"name": name, "author": author, "count": count})
    print("Book inserted successfully")

def delete_book():
    name = input("Enter the name of the book: ")
    for book in books.find({"name": name}):
        books.delete_one(book)
        print("Book deleted successfully")




welcome = '''Hello! Welcome to Library Management Program'''
options = '''Enter:\n1. List all books\n2. Checkout book\n3. Insert a new book\n4. Delete a book\nPress any other key to quit'''
print(welcome)
while True:
    print(options)
    ch = input()
    if ch=='1' :
        printf()
    elif ch=='2':
        checkout()
    elif ch=='3':
        insert()
    elif ch=='4':
        delete_book()
    else:
        print("Thank you!")
        break