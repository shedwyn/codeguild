import random


class Card:
    def __init__(self, suit, card_rank):
        """takes suit and card_val where card_val == 'Ace', '2', '3'...'King'"""
        self.suit = suit
        self.card_rank = card_rank

    def __repr__(self):
        """magic repr"""
        return 'Card({}, {})'.format(self.suit, self.card_rank)

    def score_single_card(card):
        
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
        card_score = 0
        for item in scores:
            if card.card_rank == item[0]:
                card_score = item[1]
        print(card_score)
        return card_score


class Hand:
    def __init__(self, cards):
        self.cards = cards

    def __repr__(self):
        return 'Hand({})'.format(self.cards)

    


    def give_score(user_hand):
        """return lose message if score_hand() > 21"""
  
        scoring_list = []
        
        for card in user_hand.cards:
            scoring_list.append(Card.score_single_card(card))

        print [scoring_list]

        hand_score = sum(scoring_list)

        print(hand_score)

        return hand_score




    def score_hand(hand_score):
    """returns total score of final hand"""

        if score_hand(user_hand) < 21:
            add_card_to_hand(user_hand)

        elif score_hand() == 21:
                print('winner, winner, chicken dinner!')
        else:
                print('wah, wah, wah...busted!')

def prompt_user_for_suit():
    """ask user for suit of card, return suit"""
    user_suit = input('\nWhat suit to use for card? ')

    return suit


def prompt_user_for_card():
    """ask user for hand, instantiate to Card, return instantiated card"""
    
    
    user_rank = input('Which card is it? ')
    user_card = Card(user_suit, user_rank)
    
    return user_card

def format_single_card(suit, rank):
    """ask user for rank, return rank"""
    print(
        'For ease of data entry, use the following abbreviations:',
        '\n SUITS:  clubs = cl, spades = sp, hearts = he, and diamonds = di',
        '\n CARD RANK: ace, jack, queen, king',
        '\n    cards ranked with numbers are 2 - 10'
    )

    suit = prompt_user_for_suit()
    rank = prompt_user_for_card()

    return user_card


def format_user_hand():
    


    
    return user_hand

def draw_new_card():
    """adds a card to a hand"""

    new_card = prompt_user_for_card()
    user_hand.cards.append




def schematic():
    """functions that run the program, returns nothing"""

    user_card1 = prompt_user_for_card()
    user_card2 = prompt_user_for_card()
    user_hand = Hand([user_card1, user_card2])
    print(user_card1, user_card2, user_hand)

    # suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
    # card1 = Card('cl', '9')
    # card2 = Card('he', 'ace')
    # user_hand = Hand([card1, card2])

    format_user_hand()
    #give_score(user_hand)
    #hand_score = Hand.give_score(user_hand) # store somewhere to be redrawn?


    draw_new_card()








    

    #score_hand(hand_score)

    





schematic()
