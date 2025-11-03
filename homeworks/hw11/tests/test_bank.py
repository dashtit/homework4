import pytest
from homeworks.hw11.bank_deposit.bank import Bank
from homeworks.hw11.bank_deposit.currency import CurrencyConverter
from homeworks.hw11.tests.logger_config import setup_logger


logger = setup_logger()


@pytest.mark.parametrize('client_id,name,expected', [
    ('001', 'Umpa Lumpa', True),
    ('002', 'Holly Polly', True),
])
def test_register_client(client_id, name, expected):
    bank = Bank()
    logger.info(f'Running test: test_register_client for {client_id} - {name}')
    result = bank.register_client(client_id, name)
    if result != expected:
        logger.error(f'Test: test_register_client failed for {client_id} - {name},'
                     f' expected {expected}, got {result}')
    assert result == expected
    logger.info(f'Test: test_register_client passed for {client_id} - {name}')


@pytest.mark.parametrize('client_id,name,expected', [
    ('001', 'Umpa Lumpa', False),
    ('002', 'Holly Polly', False),
])
def test_register_client_twice(client_id, name, expected):
    bank = Bank()
    logger.info(f'Running test: test_register_client_twice for {client_id} - {name}')
    bank.register_client(client_id, name)
    result = bank.register_client(client_id, name)
    if result != expected:
        logger.error(f'Test: test_register_client_twice failed for {client_id} - {name},'
                     f' expected {expected}, got {result}')
    assert result == expected
    logger.info(f'Test: test_register_client_twice passed for {client_id} - {name}')


@pytest.mark.parametrize('client_id,name,start_balance,years,expected', [
    ('001', 'Umpa Lumpa', 1000, 1, True),
    ('002', 'Holly Polly', 10000, 5, True),
])
def test_open_deposit(client_id, name, start_balance, years, expected):
    bank = Bank()
    logger.info(f'Running test: test_open_deposit for {client_id} - {name}')
    bank.register_client(client_id, name)
    result = bank.open_deposit_account(client_id, start_balance, years)
    if result != expected:
        logger.error(f'Test: test_open_deposit failed for {client_id} - {name},'
                     f' expected {expected}, got {result}')
    assert result == expected
    logger.info(f'Test: test_open_deposit passed for {client_id} - {name}')


@pytest.mark.parametrize('client_id,start_balance,years,expected', [
    ('001', 1000, 1, False),
    ('002', 10000, 5, False),
])
def test_deposit_unregister_client(client_id, start_balance, years, expected):
    bank = Bank()
    logger.info(f'Running test: test_deposit_unregister_client for {client_id}')
    result = bank.open_deposit_account(client_id, start_balance, years)
    if result != expected:
        logger.error(f'Test: test_deposit_unregister_client failed for {client_id},'
                     f' expected {expected}, got {result}')
    assert result == expected
    logger.info(f'Test: test_deposit_unregister_client passed for {client_id}')


@pytest.mark.parametrize('client_id,name,start_balance,years,expected', [
    ('001', 'Umpa Lumpa', 1000, 1, 1104.71),
    ('002', 'Holly Polly', 10000, 5, 16453.09),
])
def test_calc_interest_rate(client_id, name, start_balance, years, expected):
    bank = Bank()
    logger.info(f'Running test: test_calc_interest_rate for {client_id} - {name}')
    bank.register_client(client_id, name)
    bank.open_deposit_account(client_id, start_balance, years)
    result = bank.calc_interest_rate(client_id)
    if result != expected:
        logger.error(f'Test: test_calc_interest_rate failed for {client_id},'
                     f' expected {expected}, got {result}')
    assert result == expected
    logger.info(f'Test: test_calc_interest_rate passed for {client_id} - {name}')


@pytest.mark.parametrize('client_id,expected', [
    ('001', False),
    ('002', False),
])
def test_calc_interest_rate_unregister_client(client_id, expected):
    bank = Bank()
    logger.info(f'Running test: test_calc_interest_rate_unregister_client for {client_id}')
    result = bank.calc_interest_rate(client_id)
    if result != expected:
        logger.error(f'Test: test_calc_interest_rate_unregister_client failed for {client_id},'
                     f' expected {expected}, got {result}')
    assert result == expected
    logger.info(f'Test: test_calc_interest_rate_unregister_client passed for {client_id}')


@pytest.mark.parametrize('client_id,name,expected', [
    ('001', 'Umpa Lumpa', False),
    ('002', 'Holly Polly', False),
])
def test_calc_interest_rate_no_deposit(client_id, name, expected):
    bank = Bank()
    logger.info(f'Running test: test_calc_interest_rate_no_deposit for {client_id}')
    bank.register_client(client_id, name)
    result = bank.calc_interest_rate(client_id)
    if result != expected:
        logger.error(f'Test: test_calc_interest_rate_no_deposit failed for {client_id} - {name},'
                     f' expected {expected}, got {result}')
    assert result == expected
    logger.info(f'Test: test_calc_interest_rate_no_deposit passed for {client_id}')


@pytest.mark.parametrize('client_id,name,start_balance,years,expected', [
    ('001', 'Umpa Lumpa', 1000, 1, 1104.71),
    ('002', 'Holly Polly', 10000, 5, 16453.09),
])
def test_close_deposit(client_id, name, start_balance, years, expected):
    bank = Bank()
    logger.info(f'Running test: test_close_deposit for {client_id} - {name}')
    bank.register_client(client_id, name)
    bank.open_deposit_account(client_id, start_balance, years)
    result = bank.close_deposit(client_id)
    if result != expected:
        logger.error(f'Test: test_close_deposit failed for {client_id},'
                     f' expected {expected}, got {result}')
    assert result == expected
    logger.info(f'Test: test_close_deposit passed for {client_id} - {name}')


@pytest.mark.parametrize('client_id,expected', [
    ('001', False),
    ('002', False),
])
def test_close_deposit_unregister_client(client_id, expected):
    bank = Bank()
    logger.info(f'Running test: test_close_deposit_unregister_client for {client_id}')
    result = bank.close_deposit(client_id)
    if result != expected:
        logger.error(f'Test: test_close_deposit_unregister_client failed for {client_id},'
                     f' expected {expected}, got {result}')
    assert result == expected
    logger.info(f'Test: test_close_deposit_unregister_client passed for {client_id}')


@pytest.mark.parametrize('client_id,name,expected', [
    ('001', 'Umpa Lumpa', False),
    ('002', 'Holly Polly', False),
])
def test_close_deposit_no_deposits(client_id, name, expected):
    bank = Bank()
    logger.info(f'Running test: test_close_deposit_no_deposits for {client_id}')
    bank.register_client(client_id, name)
    result = bank.close_deposit(client_id)
    if result != expected:
        logger.error(f'Test: test_close_deposit_no_deposits failed for {client_id},'
                     f' expected {expected}, got {result}')
    assert result == expected
    logger.info(f'Test: test_close_deposit_no_deposits passed for {client_id}')


@pytest.mark.parametrize('from_curr,amount,to_curr,expected', [
    ('USD', 1000, 'BYN', (3267.7, 'BYN')),
    ('EUR', 1000, 'BYN', (3399, 'BYN')),
    ('BYN', 1000, 'USD', (306.03, 'USD')),
    ('BYN', 1000, 'EUR', (294.2, 'EUR')),
    ('USD', 1000, 'EUR', (961.37, 'EUR')),
    ('EUR', 1000, 'USD', (1040.18, 'USD')),
])
def test_converter(from_curr, amount, to_curr, expected):
    currency = CurrencyConverter()
    logger.info(f'Running test: test_converter for {from_curr}/{to_curr} - {amount}')
    result = currency.convert(from_curr, amount, to_curr)
    if result != expected:
        logger.error(f'Test: test_converter failed for {from_curr}/{to_curr},'
                     f' expected {expected}, got {result}')
    assert result == expected
    logger.info(f'Test: test_converter passed for {from_curr}/{to_curr} - {amount}')


@pytest.mark.parametrize('from_curr,amount,to_curr,expected', [
    ('USD', 1000, 'BYYN', 'Unsupported currency: {curr}'),
])
def test_cc_invalid_to_currency(from_curr, amount, to_curr, expected):
    bank = Bank()
    logger.info(f'Running test: test_cc_invalid_to_currency for {from_curr}/{to_curr} - {amount}')
    with pytest.raises(ValueError) as e:
        assert bank.exchange_currency(from_curr, amount, to_curr)
    result = str(e.value)
    if result != expected.format(curr=to_curr):
        logger.error(f'Test: test_cc_invalid_to_currency failed for {from_curr}/{to_curr},'
                     f' expected {expected}, got {result}')
    assert result == expected.format(curr=to_curr)
    logger.info(f'Test: test_cc_invalid_to_currency passed for {from_curr}/{to_curr} - {amount}')


@pytest.mark.parametrize('from_curr,amount,to_curr,expected', [
    ('USSD', 1000, 'BYN', 'Unsupported currency: {curr}'),
])
def test_cc_invalid_from_currency(from_curr, amount, to_curr, expected):
    bank = Bank()
    logger.info(f'Running test: test_cc_invalid_from_currency for {from_curr}/{to_curr} - {amount}')
    with pytest.raises(ValueError) as e:
        assert bank.exchange_currency(from_curr, amount, to_curr)
    result = str(e.value)
    if result != expected.format(curr=from_curr):
        logger.error(f'Test: test_cc_invalid_from_currency failed for {from_curr}/{to_curr},'
                     f' expected {expected}, got {result}')
    assert result == expected.format(curr=from_curr)
    logger.info(f'Test: test_cc_invalid_from_currency for {from_curr}/{to_curr} - {amount}')
