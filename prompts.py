def ui_action():
    selection = input("\n1) add new book \n2) print current \nQ) exit\nselect: ")
    return selection


def invalid_action():
    print('invalid action!')


def get_book_info():
    book_name = input("\nbook name: ")
    book_author = input("author name: ")
    book_isbn = input("ISBN: ")
    book_year = input("publishing year: ")
    return "{0}/{1}/{2}/{3}".format(book_name, book_author, book_isbn, book_year)


def confirm_book(book):
    print("Are you sure you want to add following book to library?\n" + book)
    while True:
        confirmation = input("(y/n): ")
        print(confirmation)
        if confirmation.lower() not in ("y", "n"):
            print("invalid input!")
        if confirmation.lower() == "y" or None:
            return True
        if confirmation.lower() == "n":
            return False
