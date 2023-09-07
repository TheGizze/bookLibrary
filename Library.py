from FileHandler import FileHandler


class Library:

    def __init__(self, data_source):
        self.fileHandler = FileHandler(data_source)
        self.books = self.fileHandler.read_data()

    def get_books(self):
        return self.books

    def add_book(self, book):
        self.books.append(book)
        self.fileHandler.write_data(self.books)
