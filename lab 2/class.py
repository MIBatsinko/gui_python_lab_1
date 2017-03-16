import random


class Iterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index != len(self.numbers) - 1:
            self.index += 1
        else:
            self.index = 0
        return self.numbers[self.index]


class Card(object):
    def __init__(self, rank, suit):
        assert suit in ['S', 'C', 'H', 'D'], 'error'
        assert rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'], 'error'
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)


class Deck(object):
    def __init__(self):
        self.deck = []

    def create_deck(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        # Spades, Clubs, Hearts, Diamonds
        suits = ['S', 'C', 'H', 'D']
        self.deck = [Card(r, s) for r in ranks for s in suits]
        return self.deck

    def shuffle_cards(self):
        random.shuffle(self.create_deck())

    def next_card(self):
        return Iterator(self.deck)
