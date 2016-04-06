import random


class Card:
    def __init__(self, suit, card_rank):
        """takes suit and card_val where card_val == 'Ace', '2', '3'...'King'"""
        self.suit = suit
        self.card_rank = card_rank

    def __repr__(self):
        """magic repr"""
        return 'Card({}, {})'.format(self.suit, self.card_rank)


class Hand:
    def __init__(self, cards):
        self.cards = cards

    def __repr__(self):
        return 'Hand({})'.format(self.cards)


suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']

rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

Jack = Card('Clubs', 'Jack')



def add_card_to_hand():
    """adds a card to a hand"""


def score_hand():
    """returns total score of final hand"""


def give_score():
    """return lose message if score_hand() > 21"""


def prompt_user_for_hand():
    """ask user for hand, run functions to score, return score"""
    print(
        'For ease of data entry, use the following abbreviations:',
        '\n SUITS:  Clubs = CL, Spades = SP, Hearts = HE, and Diamonds = DI',
        '\n CARD RANK: Ace = ac, Jack = ja, Queen = qu, King = ki',
        '\n    cards ranked with numbers are 2 - 10'
    )
    user_suit1 = input('\nWhat suit to use for card 1? ')
    user_rank1 = input('Which card is it? ')
    user_suit2 = input('\nWhat suit to use for card 2? ')
    user_rank2 = input('Which card is it? ')
    user_cards = [(user_suit1, user_rank1), (user_suit2, user_rank2)]
    
    return user_cards

def format_user_hand():
    user_cards = prompt_user_for_hand()
    user_card1 = Card(user_cards[0][0], user_cards[0][1])
    user_card2 = Card(user_cards[1][0], user_cards[1][1])
    user_hand = Hand([user_card1, user_card2])
    print(user_card1, user_card2, user_hand)

    return user_hand


def schematic():

    format_user_hand()


schematic()