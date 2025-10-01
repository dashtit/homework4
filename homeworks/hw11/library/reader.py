class Reader:

    def __init__(self, reader_name):
        self.reader_name = reader_name

    def reserve_book(self, book):
        return book.reserve(self.reader_name)

    def cancel_reserve(self, book):
        return book.cancel_reserve(self.reader_name)

    def get_book(self, book):
        return book.get_book(self.reader_name)

    def return_book(self, book):
        return book.return_book(self.reader_name)
