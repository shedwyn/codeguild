import random


class Card:
    def __init__(self, suit, card_val):
        """takes suit and card_val where card_val == 'Ace', '2', '3'...'King'"""
        self.suit - suit
        self.card_val = card_val
        

    def __repr__(self):
        """magic repr"""
        return 'Card({}, {})'.format(self.suit, self.card_val)

class Hand:
    def __init__(self, cards):
        self.cards = cards

    def __repr__(self):
        return 'Hand({})'.format(self.cards)

class Deck:
    def __init__(self, cards)

suits = ['Club', 'Spade', 'Heart', 'Diamond']

deck = 

  #what attributes does a card have?  what attributes does a hand have?