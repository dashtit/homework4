from homeworks.hw11.bank_deposit.currency import CurrencyConverter


class Bank:

    def __init__(self):
        self.clients = {}
        self.deposits = {}
        self.converter = CurrencyConverter()

    def register_client(self, client_id, name):
        if client_id not in self.clients:
            self.clients[client_id] = name
            return True
        return False

    def open_deposit_account(self, client_id, start_balance, years):
        if client_id not in self.clients:
            return False
        self.deposits[client_id] = {'balance': start_balance, 'years': years}
        return True

    def calc_interest_rate(self, client_id):
        if client_id not in self.clients:
            return False
        if client_id not in self.deposits:
            return False
        rate = (self.deposits[client_id]['balance'] * (1 + 0.1 / 12)
                ** (self.deposits[client_id]['years'] * 12))
        return round(rate, 2)

    def close_deposit(self, client_id):
        if client_id not in self.clients:
            return False
        if client_id not in self.deposits:
            return False
        final = self.calc_interest_rate(client_id)
        del self.deposits[client_id]
        return final

    def exchange_currency(self, from_curr, amount, to_curr='BYN'):
        return self.converter.convert(from_curr=from_curr, amount=amount, to_curr=to_curr)
