class CurrencyConverter:
    def __init__(self):
        self.rates = {
                ('USD', 'BYN'): 3.2677,
                ('EUR', 'BYN'): 3.399,
                ('BYN', 'USD'): 1 / 3.2677,
                ('BYN', 'EUR'): 1 / 3.399,
                ('USD', 'EUR'): 3.2677 / 3.399,
                ('EUR', 'USD'): 3.399 / 3.2677,
            }

    def convert(self, from_curr, amount, to_curr):
        if from_curr not in {'USD', 'EUR', 'BYN'}:
            raise ValueError(f"Unsupported currency: {from_curr}")
        if to_curr not in {'USD', 'EUR', 'BYN'}:
            raise ValueError(f"Unsupported currency: {to_curr}")
        rate = self.rates[(from_curr, to_curr)]
        converted = round(amount * rate, 2)
        return (converted, to_curr)
