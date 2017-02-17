class AbstractFactory:
    def suit(self, value):
        raise NotImplementedError()

    def rank(self, value):
        raise NotImplementedError()

class Card(AbstractFactory):
    def suit(self, value):
        return value

    def rank(self, value):
        return value

class getCard:
    def __init__(self, suit, rank):
        self.suit = Card().suit(suit)
        self.rank = Card().rank(rank)

    def __str__(self):
        return "Rank: " + self.rank + "\nSuit: " + self.suit

if __name__ == "__main__":
    ranks = ['6', '7', '8', '9', '10', 'J', 'L', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    cardNumber = 1

    for suit in suits:
        for rank in ranks:
            print("===== Card", cardNumber, "=====")
            print(getCard(suit, rank))
            cardNumber += 1
