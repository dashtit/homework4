import random


class Card:
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', 'Joker']
    masts = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, mast=None, rank=None):
        self.mast = mast
        self.rank = rank


class CardsDeck:

    def __init__(self):
        self.deck = []
        for mast in Card.masts:
            for rank in Card.ranks[:-1]:
                card = Card(mast, rank)
                self.deck.append(card)
        self.deck.append(Card(rank='Joker'))
        self.deck.append(Card(rank='Joker'))

    def shuffle(self):
        random.shuffle(self.deck)

    def _card_validator(self, number):
        if not isinstance(number, int) or number >= 54:
            raise ValueError("Error: enter a card number from 1 to 54")
        return number

    def get_card(self, number):
        validated = self._card_validator(number)
        validated = self._card_validator(validated)
        return self.deck.pop(validated - 1)

    def get_remaining_cards(self):
        return self.deck
