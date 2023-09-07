import argparse
import actions
from Library import Library
import prompts


def read_arguments():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-d", "--datafile", help="datafile to read")
    return argParser.parse_args()


def main(args):
    library = Library(args.datafile)
    while True:
        action = prompts.ui_action()
        if action not in ("1", "2", "q", "Q"):
            actions.invalid_action()
        if action in ("q", "Q"):
            actions.quit_app(library)
        if action == "1":
            actions.add_book(library)
        if action == "2":
            actions.print_books(library)


if __name__ == "__main__":
    args = read_arguments()
    main(args)
