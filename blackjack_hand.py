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

    def give_score(user_hand):
        """return lose message if score_hand() > 21"""

        scores = [
            ('ace', 1), 
            ('2', 2), 
            ('3', 3), 
            ('4', 4), 
            ('5', 5), 
            ('6', 6), 
            ('7', 7), 
            ('8', 8), 
            ('9', 9), 
            ('10', 10), 
            ('jack', 10), 
            ('queen', 10), 
            ('king', 10)
        ]
        scoring_list = []
        for card in user_hand:
            card_score = item[1] in scores if card.card_rank == item[1] for item in scores
            scoring_list.append(card_score)
        
        print(scoring_list)

        return hand_score


        # if score_hand(user_hand) < 21:
        #     add_card_to_hand(user_hand)

        # elif score_hand() == 21:
        #     print('winner, winner, chicken dinner!')
        # else:
        #     print('wah, wah, wah...busted!')

def add_card_to_hand(user_hand):
    """adds a card to a hand"""

def score_hand(user_hand, scores):
    """returns total score of final hand"""



    return None

def prompt_user_for_hand():
    """ask user for hand, run functions to score, return score"""
    print(
        'For ease of data entry, use the following abbreviations:',
        '\n SUITS:  clubs = cl, spades = sp, hearts = he, and diamonds = di',
        '\n CARD RANK: ace, jack, queen, king',
        '\n    cards ranked with numbers are 2 - 10'
    )
    user_suit = input('\nWhat suit to use for card? ')
    user_rank = input('Which card is it? ')
    user_card = (user_suit, user_rank)
    
    return user_card

def format_user_hand():
    user_card1 = prompt_user_for_hand()
    user_card2 = prompt_user_for_hand()
    user_hand = Hand([user_card1, user_card2])
    print(user_card1, user_card2, user_hand)

    return user_hand

def schematic():
    #suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
    card1 = Card('cl', '9')
    card2 = Card('he', 'ace')
    user_hand = Hand([card1, card2])
    #format_user_hand()
    #give_score(user_hand)
    Hand.give_score(user_hand)


schematic()
