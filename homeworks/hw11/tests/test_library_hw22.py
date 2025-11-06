import pytest
from homeworks.hw11.tests.logger_config import setup_logger


logger = setup_logger()


class StubBook:

    def __init__(self):
        self.title = 'The Hobbit'
        self.author = 'J. R. R. Tolkien'
        self.pages = 310
        self.isbn = '0345339681'


class FakeReader:

    def __init__(self, name):
        self.name = name
        self.reserved_books = set()
        self.borrowed_books = set()

    def reserve_book(self, book):
        if getattr(book, 'is_reserved', False):
            return False
        book.is_reserved = True
        book.reserved_by = self
        self.reserved_books.add(book)
        return True

    def get_book(self, book):
        if getattr(book, 'is_reserved', False) and getattr(book, 'reserved_by', None) != self:
            return False
        if getattr(book, 'is_borrowed', False):
            return False
        if getattr(book, 'reserved_by', False) == self:
            delattr(book, 'is_reserved')
            delattr(book, 'reserved_by')
            self.reserved_books.discard(book)
        book.is_borrowed = True
        book.borrowed_by = self
        self.borrowed_books.add(book)
        return True

    def cancel_reserve(self, book):
        if getattr(book, 'is_reserved', False) and getattr(book, 'reserved_by', None) == self:
            delattr(book, 'is_reserved')
            delattr(book, 'reserved_by')
            self.reserved_books.discard(book)
            return True
        return False

    def return_book(self, book):
        if getattr(book, 'borrowed_by', None) != self:
            return False
        delattr(book, 'is_borrowed')
        delattr(book, 'borrowed_by')
        self.borrowed_books.discard(book)
        return True


class TestLibrary:

    @pytest.fixture
    def book(self):
        return StubBook()

    @pytest.fixture
    def reader(self):
        return FakeReader('Umpa Lumpa')

    @pytest.fixture
    def second_reader(self):
        return FakeReader('Tumba Umba')

    def test_reader_reserve_book(self, book, reader):
        logger.info('Running test: test_reader_reserve_book')
        result = reader.reserve_book(book)
        if not result:
            logger.error(f'Test: test_reader_reserve_book failed,'
                         f' expected True, got {result}')
        assert result is True
        logger.info('Test: test_reader_reserve_book passed')

    def test_reader_get_book(self, book, reader):
        logger.info('Running test: test_reader_get_reserved_book')
        result = reader.get_book(book)
        if not result:
            logger.error(f'Test: test_reader_get_reserved_book failed,'
                         f' expected True, got {result}')
        assert result is True
        logger.info('Test: test_reader_get_reserved_book passed')

    def test_reader_get_gotten_book(self, book, reader, second_reader):
        logger.info('Running test: test_reader_return_book')
        reader.get_book(book)
        result = second_reader.get_book(book)
        if result:
            logger.error(f'Test: test_reader_get_gotten_book failed,'
                         f' expected False, got {result}')
        assert result is False
        logger.info('Test: test_reader_get_gotten_book passed')

    def test_reader_get_reserved_book(self, book, reader, second_reader):
        logger.info('Running test: test_reader_get_reserved_book')
        reader.reserve_book(book)
        result = second_reader.get_book(book)
        if result:
            logger.error(f'Test: test_reader_get_reserved_book failed,'
                         f' expected False, got {result}')
        assert result is False
        logger.info('Test: test_reader_get_reserved_book passed')

    def test_reader_reserve_and_get_book(self, book, reader):
        logger.info('Running test: test_reader_reserve_and_get_book')
        reader.reserve_book(book)
        result = reader.get_book(book)
        if not result:
            logger.error(f'Test: test_reader_reserve_and_get_book failed,'
                         f' expected True, got {result}')
        assert result is True
        logger.info('Test: test_reader_reserve_and_get_book passed')

    def test_reader_cancel_reserve(self, book, reader):
        logger.info('Running test: test_reader_cancel_reserve')
        reader.reserve_book(book)
        result = reader.cancel_reserve(book)
        if not result:
            logger.error(f'Test: test_reader_cancel_reserve failed,'
                         f' expected True, got {result}')
        assert result is True
        logger.info('Test: test_reader_cancel_reserve passed')

    def test_reader_cancel_no_reserve(self, book, reader):
        logger.info('Running test: test_reader_cancel_no_reserve')
        result = reader.cancel_reserve(book)
        if result:
            logger.error(f'Test: test_reader_cancel_no_reserve failed,'
                         f' expected False, got {result}')
        assert result is False
        logger.info('Test: test_reader_cancel_no_reserve passed')

    def test_reader_cancel_wrong_reserve(self, book, reader, second_reader):
        logger.info('Running test: test_reader_cancel_wrong_reserve')
        reader.reserve_book(book)
        result = second_reader.cancel_reserve(book)
        if result:
            logger.error(f'Test: test_reader_cancel_wrong_reserve failed,'
                         f' expected False, got {result}')
        assert result is False
        logger.info('Test: test_reader_cancel_wrong_reserve passed')

    def test_reader_cancel_reserve_after_got_book(self, book, reader):
        logger.info('Running test: test_reader_cancel_reserve_after_got_book')
        reader.reserve_book(book)
        reader.get_book(book)
        result = reader.cancel_reserve(book)
        if result:
            logger.error(f'Test: test_reader_cancel_reserve_after_got_book failed,'
                         f' expected False, got {result}')
        assert result is False
        logger.info('Test: test_reader_cancel_reserve_after_got_book passed')

    def test_reader_return_book(self, book, reader):
        logger.info('Running test: test_reader_return_book')
        reader.get_book(book)
        result = reader.return_book(book)
        if not result:
            logger.error(f'Test: test_reader_return_book failed,'
                         f' expected True, got {result}')
        assert result is True
        logger.info('Test: test_reader_return_book passed')

    def test_reader_return_wrong_book(self, book, reader, second_reader):
        logger.info('Running test: test_reader_return_wrong_book')
        reader.get_book(book)
        result = second_reader.return_book(book)
        if result:
            logger.error(f'Test: test_reader_return_wrong_book failed,'
                         f' expected False, got {result}')
        assert result is False
        logger.info('Test: test_reader_return_wrong_book passed')
