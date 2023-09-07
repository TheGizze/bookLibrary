from src.BookLibrary.FileHandler import FileHandler


class Library:

    def __init__(self, data_source):
        self.fileHandler = FileHandler(data_source)
        self.books = self.fileHandler.read_data()

    def get_books(self):
        return self.books

    def add_book(self, book):
        self.books.append(book)

    def write_library_to_file(self):
        self.fileHandler.write_data(self.books)

    def arrange_books_by_year(self):
        """
        splits the line with '/' as a separator and uses the part with publishing year to sort
        [0] book name
        [1] author
        [2] isbn
        [3] year
        """
        self.books.sort(key=lambda x: x.split('/')[3])
