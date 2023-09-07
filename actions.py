import prompts


def print_books(library):
    library.arrange_books_by_year()  # arrange books before printing
    print("")  # prints emptyline before printing books
    for book in library.get_books():
        print(book)


def add_book(library):
    book = prompts.get_book_info()
    confirmed = prompts.confirm_book(book)
    if confirmed:
        library.add_book(book)

def invalid_action():
    prompts.invalid_action()
