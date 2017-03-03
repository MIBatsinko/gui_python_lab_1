import random


class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)


class Deck(object):
    def __init__(self):
        ranks = "23456789TJQKA"
        # Spades, Clubs, Hearts, Diamonds
        suits = "SCHD"
        self.cards = [Card(r, s) for r in ranks for s in suits]

    def get_cards(self):
        for i in range(52):
            print(self.cards[i])

    def shuffle_cards(self):
        random.shuffle(self.cards)


if __name__ == "__main__":
    a = Deck()
    a.get_cards()
    print('\n\nAfter shuffle:')
    a.shuffle_cards()
    a.get_cards()
