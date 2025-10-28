import unittest
from homeworks.hw11.bank_deposit.bank import Bank
from homeworks.hw11.bank_deposit.currency import CurrencyConverter
from homeworks.hw11.library.book import Book
from homeworks.hw11.library.reader import Reader


class TestBankDeposit(unittest.TestCase):
    def test_register_client(self):
        bank = Bank()
        self.assertTrue(bank.register_client('001', 'Umpa Lumpa'))
        self.assertTrue(bank.register_client('002', 'Holly Polly'))

    def test_register_client_twice(self):
        bank = Bank()
        self.assertTrue(bank.register_client('001', 'De Lulu'))
        self.assertFalse(bank.register_client('001', 'De Lulu'))

    def test_open_deposit(self):
        bank = Bank()
        bank.register_client('001', 'Umpa Lumpa')
        self.assertTrue(bank.open_deposit_account('001', 1000, 1))

    def test_deposit_unregister_client(self):
        bank = Bank()
        self.assertFalse(bank.open_deposit_account('001', 10000, 10))

    def test_calc_interest_rate(self):
        bank = Bank()
        bank.register_client('001', 'Umpa Lumpa')
        bank.open_deposit_account('001', 1000, 1)
        self.assertEqual(bank.calc_interest_rate('001'), 1104.71)

    def test_calc_interest_rate_unregister_client(self):
        bank = Bank()
        self.assertFalse(bank.calc_interest_rate('003'))

    def test_calc_interest_rate_no_deposit(self):
        bank = Bank()
        bank.register_client('001', 'Umpa Lumpa')
        self.assertFalse(bank.calc_interest_rate('001'))

    def test_close_deposit(self):
        bank = Bank()
        bank.register_client('001', 'Umpa Lumpa')
        bank.open_deposit_account('001', 1000, 1)
        self.assertEqual(bank.close_deposit('001'), 1104.71)

    def test_close_deposit_unregister_client(self):
        bank = Bank()
        self.assertFalse(bank.close_deposit('001'))

    def test_close_deposit_no_deposits(self):
        bank = Bank()
        bank.register_client('001', 'Umpa Lumpa')
        self.assertFalse(bank.close_deposit('004'))

    def test_converter(self):
        currency = CurrencyConverter()
        self.assertEqual(currency.convert('USD', 1000, 'BYN'), (3267.7, 'BYN'))
        self.assertEqual(currency.convert('EUR', 1000, 'BYN'), (3399, 'BYN'))
        self.assertEqual(currency.convert('BYN', 1000, 'USD'), (306.03, 'USD'))
        self.assertEqual(currency.convert('BYN', 1000, 'EUR'), (294.2, 'EUR'))
        self.assertEqual(currency.convert('USD', 1000, 'EUR'), (961.37, 'EUR'))
        self.assertEqual(currency.convert('EUR', 1000, 'USD'), (1040.18, 'USD'))

    def test_cc_invalid_to_currency(self):
        bank = Bank()
        with self.assertRaises(ValueError):
            bank.exchange_currency('USD', 1000, 'BYYN')

    def test_cc_invalid_from_currency(self):
        bank = Bank()
        with self.assertRaises(ValueError):
            bank.exchange_currency('USSD', 1000, 'BYN')


class TestLibrary(unittest.TestCase):
    def test_reader_reserve_book(self):
        book = Book('The Hobbit', 'J. R. R. Tolkien', 310, '0345339681')
        reader = Reader('Umpa Lumpa')
        self.assertTrue(reader.reserve_book(book))

    def test_reader_get_book(self):
        book = Book('The Hobbit', 'J. R. R. Tolkien', 310, '0345339681')
        reader = Reader('Umpa Lumpa')
        self.assertTrue(reader.get_book(book))

    def test_reader_get_gotten_book(self):
        book = Book('The Hobbit', 'J. R. R. Tolkien', 310, '0345339681')
        reader = Reader('Umpa Lumpa')
        reader2 = Reader('Tumba Umba')
        reader.get_book(book)
        self.assertFalse(reader2.get_book(book))

    def test_reader_get_reserved_book(self):
        book = Book('The Hobbit', 'J. R. R. Tolkien', 310, '0345339681')
        reader = Reader('Umpa Lumpa')
        reader2 = Reader('Tumba Umba')
        reader.reserve_book(book)
        self.assertFalse(reader2.get_book(book))

    def test_reader_reserve_and_get_book(self):
        book = Book('The Hobbit', 'J. R. R. Tolkien', 310, '0345339681')
        reader = Reader('Umpa Lumpa')
        reader.reserve_book(book)
        self.assertTrue(reader.get_book(book))

    def test_reader_cancel_reserve(self):
        book = Book('The Hobbit', 'J. R. R. Tolkien', 310, '0345339681')
        reader = Reader('Umpa Lumpa')
        reader.reserve_book(book)
        self.assertTrue(reader.cancel_reserve(book))

    def test_reader_cancel_no_reserve(self):
        book = Book('The Hobbit', 'J. R. R. Tolkien', 310, '0345339681')
        reader = Reader('Umpa Lumpa')
        self.assertFalse(reader.cancel_reserve(book))

    def test_reader_cancel_wrong_reserve(self):
        book = Book('The Hobbit', 'J. R. R. Tolkien', 310, '0345339681')
        reader = Reader('Umpa Lumpa')
        reader2 = Reader('Tumba Umba')
        reader.reserve_book(book)
        self.assertFalse(reader2.cancel_reserve(book))

    def test_reader_cancel_reserve_after_got_book(self):
        book = Book('The Hobbit', 'J. R. R. Tolkien', 310, '0345339681')
        reader = Reader('Umpa Lumpa')
        reader.reserve_book(book)
        reader.get_book(book)
        self.assertFalse(reader.cancel_reserve(book))

    def test_reader_return_book(self):
        book = Book('The Hobbit', 'J. R. R. Tolkien', 310, '0345339681')
        reader = Reader('Umpa Lumpa')
        reader.get_book(book)
        self.assertTrue(reader.return_book(book))

    def test_reader_return_wrong_book(self):
        book = Book('The Hobbit', 'J. R. R. Tolkien', 310, '0345339681')
        reader = Reader('Umpa Lumpa')
        reader2 = Reader('Tumba Umba')
        reader.get_book(book)
        self.assertFalse(reader2.return_book(book))

    def test_readers_using_library(self):
        book = Book('The Hobbit', 'J. R. R. Tolkien', 310, '0345339681')
        reader = Reader('Umpa Lumpa')
        reader2 = Reader('Tumba Umba')
        self.assertTrue(reader.reserve_book(book))
        self.assertTrue(reader.cancel_reserve(book))
        self.assertTrue(reader2.get_book(book))
        self.assertTrue(reader2.return_book(book))
        self.assertTrue(reader.reserve_book(book))
        self.assertTrue(reader.get_book(book))
        self.assertTrue(reader.return_book(book))
