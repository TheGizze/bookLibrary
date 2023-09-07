import prompts
def print_books(library):
    print("")  # prints emptyline before printing books
    for book in library.get_books():
        print(book)


def add_book(library):
    book = prompts.get_book_info()
    library.add_book(book)


def invalid_action():
    prompts.invalid_action()
