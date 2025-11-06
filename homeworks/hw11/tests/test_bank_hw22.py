from unittest.mock import MagicMock
import random
import pytest
from homeworks.hw11.tests.logger_config import setup_logger


logger = setup_logger()


class FakeBank:

    def __init__(self):
        self.clients = {}
        self.deposits = {}

    def register_client(self, client_id, name):
        if client_id in self.clients:
            return False
        self.clients[client_id] = name
        return True

    def open_deposit_account(self, client_id, amount, years):
        if client_id not in self.clients:
            return False
        self.deposits[client_id] = (amount, years)
        return True

    def calc_interest_rate(self, client_id):
        if client_id not in self.deposits:
            return False
        amount, years = self.deposits[client_id]
        return round(amount * (1.1 ** years), 2)

    def close_deposit(self, client_id):
        if client_id not in self.deposits:
            return False
        amount, years = self.deposits.pop(client_id)
        return round(amount * (1.1 ** years), 2)


class TestBank:

    @pytest.fixture
    def mock_converter(self):
        mock = MagicMock()
        mock.convert.return_value = (3267.7, 'BYN')
        return mock

    @pytest.fixture
    def bank(self):
        return FakeBank()

    @pytest.fixture
    def client(self, bank):
        bank.register_client('001', 'Umpa Lumpa')
        return '001'

    def test_register_client(self, bank):
        logger.info('Running test: test_register_client')
        result = bank.register_client('002', 'Tumba Umba')
        if not result:
            logger.error(f'Test: test_register_client failed, expected True, got {result}')
        assert result is True
        assert '002' in bank.clients
        logger.info('Test: test_register_client passed')

    def test_register_client_twice(self, bank, client):
        logger.info('Running test: test_register_client_twice')
        result = bank.register_client(client, 'Tumba Umba')
        if result:
            logger.error(f'Test: test_register_client_twice failed, expected False, got {result}')
        assert result is False
        logger.info('Test: test_register_client_twice passed')

    def test_open_deposit(self, bank, client):
        logger.info('Running test: test_open_deposit')
        result = bank.open_deposit_account(client, 1000, 1)
        if not result:
            logger.error(f'Test: test_open_deposit failed, expected True, got {result}')
        assert result is True
        logger.info('Test: test_open_deposit passed')

    def test_deposit_unregister_client(self, bank):
        logger.info('Running test: test_deposit_unregister_client')
        result = bank.open_deposit_account('001', 1000, 1)
        if result:
            logger.error(f'Test: test_deposit_unregister_client failed,'
                         f' expected False, got {result}')
        assert result is False
        logger.info('Test: test_deposit_unregister_client passed')

    def test_calc_interest_rate(self, bank, client):
        logger.info('Running test: test_calc_interest_rate')
        bank.open_deposit_account(client, 10000, 5)
        result = bank.calc_interest_rate(client)
        if result != 16105.1:
            logger.error(f'Test: test_calc_interest_rate failed,'
                         f' expected 16105.1, got {result}')
        assert result == 16105.1
        logger.info('Test: test_calc_interest_rate passed')

    def test_calc_interest_rate_unregister_client(self, bank):
        logger.info('Running test: test_calc_interest_rate_unregister_client')
        result = bank.open_deposit_account('001', 10000, 5)
        if result:
            logger.error(f'Test: test_calc_interest_rate_unregister_client failed,'
                         f' expected False, got {result}')
        assert result is False
        logger.info('Test: test_calc_interest_rate_unregister_client passed')

    def test_calc_interest_rate_no_deposit(self, bank, client):
        logger.info('Running test: test_calc_interest_rate_no_deposit')
        result = bank.calc_interest_rate(client)
        if result:
            logger.error(f'Test: test_calc_interest_rate_no_deposit failed,'
                         f' expected False, got {result}')
        assert result is False
        logger.info('Test: test_calc_interest_rate_no_deposit passed')

    def test_close_deposit(self, bank, client):
        logger.info('Running test: test_close_deposit')
        bank.open_deposit_account(client, 1000, 1)
        result = bank.close_deposit(client)
        if result != 1100.0:
            logger.error(f'Test: test_close_deposit failed,'
                         f' expected 1100.0, got {result}')
        assert result == 1100.0
        logger.info('Test: test_close_deposit passed')

    def test_close_deposit_unregister_client(self, bank):
        logger.info('Running test: test_close_deposit_unregister_client')
        result = bank.close_deposit('001')
        if result:
            logger.error(f'Test: test_close_deposit_unregister_client failed,'
                         f' expected False, got {result}')
        assert result is False
        logger.info('Test: test_close_deposit_unregister_client passed')

    def test_close_deposit_no_deposits(self, bank, client):
        logger.info('Running test: test_close_deposit_no_deposits')
        result = bank.close_deposit(client)
        if result:
            logger.error(f'Test: test_close_deposit_no_deposits failed,'
                         f' expected False, got {result}')
        assert result is False
        logger.info('Test: test_close_deposit_no_deposits passed')

    def test_convert_usd_to_byn(self, mock_converter):
        logger.info('Running test: test_convert_usd_to_byn')
        result = mock_converter.convert('USD', 1000, 'BYN')
        if result != (3267.7, 'BYN'):
            logger.error(f'Test: test_convert_usd_to_byn failed,'
                         f' expected (3267.7, "BYN"), got {result}')
        assert result == (3267.7, 'BYN')
        mock_converter.convert.assert_called_once_with('USD', 1000, 'BYN')
        logger.info('Test: test_convert_usd_to_byn passed')

    def test_convert_eur_to_usd(self, mock_converter):
        logger.info('Running test: test_convert_eur_to_usd')
        mock_converter.convert.return_value = (1040.18, 'USD')
        result = mock_converter.convert('EUR', 1000, 'USD')
        if result != (1040.18, 'USD'):
            logger.error(f'Test: test_convert_eur_to_usd failed'
                         f' expected (1040.18, "USD"), got {result},')
        assert result == (1040.18, 'USD')
        mock_converter.convert.assert_called_once_with('EUR', 1000, 'USD')
        logger.info('Test: test_convert_eur_to_usd passed')

    def test_convert_unsupported_currency(self, mock_converter):
        logger.info('Running test: test_convert_unsupported_currency')
        mock_converter.convert.side_effect = ValueError('Unsupported currency: BYYN')
        with pytest.raises(ValueError) as e:
            mock_converter.convert('USD', 1000, 'BYYN')
        if str(e.value) != 'Unsupported currency: BYYN':
            logger.error(f'Test: test_convert_unsupported_currency failed,'
                         f' expected message "Unsupported currency: BYYN", got {str(e.value)}')
        assert str(e.value) == 'Unsupported currency: BYYN'
        mock_converter.convert.assert_called_once_with('USD', 1000, 'BYYN')
        logger.info('Test: test_convert_unsupported_currency passed')

    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    def test_unstable_converter_usd_byn(self, mock_converter):
        logger.info('Running test: test_unstable_converter_eur_usd (flaky)')
        if random.choice([True, False]):
            mock_converter.convert.side_effect = ValueError('Connection failed')
            logger.warning('Simulating unstable behavior, returning Connection error')
            logger.error('Simulating unstable behavior, failing test')
            wrong_result = mock_converter.convert('USD', 1000, 'BYN')
            assert wrong_result == (3267.7, 'BYN')
        else:
            result = mock_converter.convert('USD', 1000, 'BYN')
            assert result == (3267.7, 'BYN')
            logger.info('Test: test_unstable_converter_eur_usd passed')
