class Book:

    def __init__(self, book_name, author, num_pages, isbn):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.book_status = {'reserved': None, 'in_hand': None}

    def reserve(self, reader_name):
        if self.book_status['reserved'] is not None:
            return False
        self.book_status['reserved'] = reader_name
        return True

    def cancel_reserve(self, reader_name):
        if self.book_status['reserved'] == reader_name:
            self.book_status['reserved'] = None
            return True
        return False

    def get_book(self, reader_name):
        if self.book_status['in_hand'] is None:
            if self.book_status['reserved'] is None or self.book_status['reserved'] == reader_name:
                self.book_status['in_hand'] = reader_name
                self.book_status['reserved'] = None
                return True
        return False

    def return_book(self, reader_name):
        if self.book_status['in_hand'] == reader_name:
            self.book_status['in_hand'] = None
            return True
        return False
