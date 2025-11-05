import pytest
from homeworks.hw11.bank_deposit.bank import Bank
from homeworks.hw11.bank_deposit.currency import CurrencyConverter
from homeworks.hw11.tests.logger_config import setup_logger


logger = setup_logger()


class TestBank:

    @pytest.fixture
    def bank(self):
        return Bank()

    @pytest.fixture
    def client(self, bank):
        client_id = '001'
        bank.register_client(client_id, 'Umpa Lumpa')
        return client_id

    @pytest.fixture
    def converter(self):
        return CurrencyConverter()

    def test_register_client(self, bank, client):
        logger.info(f'Running test: test_register_client for {client}')
        if client not in bank.clients:
            logger.error(f'Test: test_register_client failed for {client},'
                         f' expected True, got False')
        assert client in bank.clients
        logger.info(f'Test: test_register_client passed for {client}')

    def test_register_client_twice(self, bank, client):
        logger.info(f'Running test: test_register_client_twice for {client}')
        result = bank.register_client('001', 'Tumba Umba')
        if result is not False:
            logger.error(f'Test: test_register_client_twice failed for {client},'
                         f' expected False, got {result}')
        assert result is False
        logger.info(f'Test: test_register_client_twice passed for {client}')

    def test_open_deposit(self, bank, client):
        logger.info(f'Running test: test_open_deposit for {client}')
        result = bank.open_deposit_account(client, 1000, 1)
        if result is not True:
            logger.error(f'Test: test_open_deposit failed for {client},'
                         f' expected True, got {result}')
        assert result is True
        logger.info(f'Test: test_open_deposit passed for {client}')

    def test_deposit_unregister_client(self, bank):
        logger.info('Running test: test_deposit_unregister_client')
        result = bank.open_deposit_account('001', 1000, 1)
        if result is not False:
            logger.error(f'Test: test_deposit_unregister_client failed,'
                         f' expected False, got {result}')
        assert result is False
        logger.info('Test: test_deposit_unregister_client passed')

    def test_calc_interest_rate(self, bank, client):
        logger.info(f'Running test: test_calc_interest_rate for {client}')
        bank.open_deposit_account(client, 10000, 5)
        result = bank.calc_interest_rate(client)
        if result != 16453.09:
            logger.error(f'Test: test_calc_interest_rate failed for {client},'
                         f' expected 16453.09, got {result}')
        assert result == 16453.09
        logger.info(f'Test: test_calc_interest_rate passed for {client}')

    def test_calc_interest_rate_unregister_client(self, bank):
        logger.info('Running test: test_calc_interest_rate_unregister_client')
        result = bank.calc_interest_rate('001')
        if result is not False:
            logger.error(f'Test: test_calc_interest_rate_unregister_client failed,'
                         f' expected False, got {result}')
        assert result is False
        logger.info('Test: test_calc_interest_rate_unregister_client passed')

    def test_calc_interest_rate_no_deposit(self, bank, client):
        logger.info(f'Running test: test_calc_interest_rate_no_deposit for {client}')
        result = bank.calc_interest_rate(client)
        if result is not False:
            logger.error(f'Test: test_calc_interest_rate_no_deposit failed for {client},'
                         f' expected False, got {result}')
        assert result is False
        logger.info(f'Test: test_calc_interest_rate_no_deposit passed for {client}')

    def test_close_deposit(self, bank, client):
        logger.info(f'Running test: test_close_deposit for {client}')
        bank.open_deposit_account(client, 1000, 1)
        result = bank.close_deposit(client)
        if result != 1104.71:
            logger.error(f'Test: test_close_deposit failed for {client},'
                         f' expected 1104.71, got {result}')
        assert result == 1104.71
        logger.info(f'Test: test_close_deposit passed for {client}')

    def test_close_deposit_unregister_client(self, bank):
        logger.info('Running test: test_close_deposit_unregister_client')
        result = bank.close_deposit('001')
        if result is not False:
            logger.error(f'Test: test_close_deposit_unregister_client failed,'
                         f' expected False, got {result}')
        assert result is False
        logger.info('Test: test_close_deposit_unregister_client passed')

    def test_close_deposit_no_deposits(self, bank, client):
        logger.info(f'Running test: test_close_deposit_no_deposits for {client}')
        result = bank.close_deposit(client)
        if result is not False:
            logger.error(f'Test: test_close_deposit_no_deposits failed for {client},'
                         f' expected False, got {result}')
        assert result is False
        logger.info(f'Test: test_close_deposit_no_deposits passed for {client}')

    def test_converter_usd_byn(self, converter):
        logger.info('Running test: test_converter for USD/BYN, amount - 1000')
        result = converter.convert('USD', 1000, 'BYN')
        if result != (3267.7, 'BYN'):
            logger.error(f'Test: test_converter failed for USD/BYN, amount - 1000,'
                         f' expected (3267.7, "BYN"), got {result}')
        assert result == (3267.7, 'BYN')
        logger.info('Test: test_converter passed for USD/BYN, amount - 1000')

    def test_converter_eur_byn(self, converter):
        logger.info('Running test: test_converter for EUR/BYN, amount - 1000')
        result = converter.convert('EUR', 1000, 'BYN')
        if result != (3399.0, 'BYN'):
            logger.error(f'Test: test_converter failed for EUR/BYN, amount - 1000,'
                         f' expected (3399, "BYN"), got {result}')
        assert result == (3399.0, 'BYN')
        logger.info('Test: test_converter passed for EUR/BYN, amount - 1000')

    def test_converter_eur_usd(self, converter):
        logger.info('Running test: test_converter for EUR/USD, amount - 1000')
        result = converter.convert('EUR', 1000, 'USD')
        if result != (1040.18, 'USD'):
            logger.error(f'Test: test_converter failed for EUR/USD, amount - 1000,'
                         f' expected (1040.18, "USD"), got {result}')
        assert result == (1040.18, 'USD')
        logger.info('Test: test_converter passed for EUR/USD, amount - 1000')

    def test_cc_invalid_to_currency(self, bank):
        logger.info('Running test: test_cc_invalid_to_currency - USD/BYYN')
        with pytest.raises(ValueError) as e:
            assert bank.exchange_currency('USD', 1000, 'BYYN')
        result = str(e.value)
        if result != 'Unsupported currency: BYYN':
            logger.error(f'Test: test_cc_invalid_to_currency failed for USD/BYYN,'
                         f' expected message - "Unsupported currency: BYYN", got {result}')
        assert result == 'Unsupported currency: BYYN'
        logger.info('Test: test_cc_invalid_to_currency passed for USD/BYYN')

    def test_cc_invalid_from_currency(self, bank):
        logger.info('Running test: test_cc_invalid_from_currency for USSD/BYN')
        with pytest.raises(ValueError) as e:
            assert bank.exchange_currency('USSD', 1000, 'BYN')
        result = str(e.value)
        if result != 'Unsupported currency: USSD':
            logger.error(f'Test: test_cc_invalid_from_currency failed for USSD/BYN,'
                         f' expected message - "Unsupported currency: USSD", got {result}')
        assert result == 'Unsupported currency: USSD'
        logger.info('Test: test_cc_invalid_from_currency for USSD/BYN')
