import random

class Card:
    def __init__(self, value=0):
        self.value = value
    def getValue(self):
        return self.value

class PlayingCard(Card):
    def __init__(self, suit="", value=0):
        super().__init__(value)
        self.suit = suit
    def getValue(self):
        return self.value

class Deck:
    def __init__(self):
        self.cards = []
    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            return None
    def shuffle(self):
        tmpDeck = []
        for x in range(0, int(len(self.cards))):
            tmpCardIndex = int(random.random()*len(self.cards))
            tmpDeck.append(self.cards[tmpCardIndex])
            self.cards.pop(tmpCardIndex)
        self.cards = tmpDeck

class PlayingCardDeck(Deck):
    def __init__(self):
        self.cards = []
        self.suits = ["hearts", "diamonds", "spades", "clubs"]
        for x in self.suits:
            for y in range(1, 14):
                self.cards.append(PlayingCard(x, y))
