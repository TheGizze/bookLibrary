import argparse
import sys
from FileHandler import FileHandler
import Library
def read_arguments():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-d", "--datafile", help="datafile to read")
    return argParser.parse_args()


def main(args):
    library = Library(args.datafile)
    while True:
        selection = input("\n1) add new book \n2) print current \nQ) exit\nselect: ")
        if selection not in ("1", "2", "q", "Q"):
            print('invalid action!')
        if selection in ("q", "Q"):
            sys.exit()
        if selection == "1":
           pass
        if selection == "2":
            books = library.get_books()
            for book in books:
                print(book)


if __name__ == "__main__":
    args = read_arguments()
    main(args)
