from CardGame import PlayingCardDeck

deck = PlayingCardDeck()
deck.shuffle()

print(deck.deal().suit)
