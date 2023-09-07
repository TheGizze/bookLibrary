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