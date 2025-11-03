import pytest
from homeworks.hw11.library.book import Book
from homeworks.hw11.library.reader import Reader
from homeworks.hw11.tests.logger_config import setup_logger


logger = setup_logger()


class TestLibrary:

    @pytest.fixture
    def book(self):
        return Book('The Hobbit', 'J. R. R. Tolkien', 310, '0345339681')


    @pytest.fixture
    def reader(self):
        return Reader('Umpa Lumpa')


    @pytest.fixture
    def second_reader(self):
        return Reader('Tumba Umba')


    def test_reader_reserve_book(self, book, reader):
        logger.info('Running test: test_reader_reserve_book')
        result = reader.reserve_book(book)
        if not result:
            logger.error(f'Test: test_reader_reserve_book failed,'
                         f' expected True, got {result}')
        assert result is True
        logger.info('Test: test_reader_reserve_book passed')


    def test_reader_get_book(self, book, reader):
        logger.info('Running test: test_reader_get_book')
        result = reader.reserve_book(book)
        if not result:
            logger.error(f'Test: test_reader_get_book failed,'
                         f' expected True, got {result}')
        assert result is True
        logger.info('Test: test_reader_get_book passed')


    def test_reader_get_gotten_book(self, book, reader, second_reader):
        logger.info('Running test: test_reader_get_gotten_book')
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
