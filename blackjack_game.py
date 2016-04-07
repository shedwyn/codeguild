import random


class Card:
    suits = ['clubs', 'spades', 'hearts', 'diamonds']
    rank = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']

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

    def calc_hand_score(self):
        """take in hand, tally current hand, return total score"""
        rank_to_score = {
            'ace': 1, 
            '2': 2, 
            '3': 3, 
            '4': 4, 
            '5': 5, 
            '6': 6, 
            '7': 7, 
            '8': 8, 
            '9': 9, 
            '10': 10, 
            'jack': 10, 
            'queen': 10, 
            'king': 10
        }
        scoring_list = []
        for card in self.cards:
            scoring_list.append(rank_to_score[card.card_rank])
        hand_score = sum(scoring_list)
        for card in self.cards:
            if card.card_rank == 'ace' and (hand_score +10) <= 21:
                hand_score += 10
        return hand_score

def Deck:
    def __init__(self, cards):
        self.cards = cards

    def __repr__(self, cards):
        return 'Deck({})'.format(self.cards)


def prompt_user_for_suit():
    """ask user for suit of card, return suit"""
    return input('\nWhat suit to use for card? ')

def prompt_user_for_rank():
    """ask user for rank, return rank"""
    return input('\nWhich card is it? ')

def create_deck():
    """takes nothing, creates deck, returns deck"""



    return





def deal_initial_hand_cards():


    return hand



def format_single_card():
    """takes nothing, prompts for card variables, returns instantiated card"""
    print(
        'For ease of data entry, use the following abbreviations:',
        '\n SUITS:  clubs = cl, spades = sp, hearts = he, and diamonds = di',
        '\n CARD RANK: ace, jack, queen, king',
        '\n    cards ranked with numbers are 2 - 10'
    )
    card_suit = prompt_user_for_suit()
    card_rank = prompt_user_for_rank()
    user_card = Card(card_suit, card_rank)
    return user_card

def format_user_hand(user_card1, user_card2):
    """takes in initial deal cards, instantiates to Hand, returns instatiated hand"""
    return Hand([user_card1, user_card2])

def draw_new_card():
    """takes nothing, creates new card, returns updated hand"""
    return format_single_card()

def add_card_to_hand(user_hand):
    """takes new card and user_hand, adds card to user_hand, returns new_hand"""
    new_card = draw_new_card()
    user_hand.cards.append(new_card)
    print('You are now holding these cards:  ', user_hand)
    produce_final_score(user_hand)
    return None

def produce_final_score(user_hand):
    """returns total score of final hand"""  
    score = user_hand.calc_hand_score()
    print('Your score is:  ', score)
    if score < 21:
        add_card_to_hand(user_hand)
    elif user_hand.calc_hand_score() == 21:
        print('winner, winner, chicken dinner!')   
    else:
        print('wah, wah, wah...busted!')

def schematic():
    """functions that run the program, returns nothing"""
    user_card1 = format_single_card()
    user_card2 = format_single_card()
    user_hand = format_user_hand(user_card1, user_card2) 
    print('You were dealt these cards:  ', user_hand)
    produce_final_score(user_hand)


schematic()
# hand = Hand([Card('cl', '2'), Card('cl', 'ace')])
# produce_final_score(hand)
