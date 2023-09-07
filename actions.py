import prompts
def print_books(library):
    print("")  # prints emptyline before printing books
    for book in library.get_books():
        print(book)


def add_book(library):
    book_name = input("\nbook name: ")
    book_author = input("author name: ")
    book_isbn = input("ISBN: ")
    book_year = input("publishing year: ")
    book = "{0}/{1}/{2}/{3}".format(book_name, book_author, book_isbn, book_year)
    library.add_book(book)


def invalid_action():
    prompts.invalid_action()
