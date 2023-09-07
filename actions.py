def print_books(library):
    print("")  # prints emptyline before printing books
    for book in library.get_books():
        print(book)