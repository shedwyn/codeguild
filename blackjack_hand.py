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
        #card_score = 0
        for item in scores:
            if card.card_rank == item[0]:
                card_score = item[1]
        return card_score


class Hand:
    def __init__(self, cards):
        self.cards = cards

    def __repr__(self):
        return 'Hand({})'.format(self.cards)

    def give_score(user_hand):
        """take in hand, tally current hand, return total score"""
  
        scoring_list = []
        
        for card in user_hand.cards:
            scoring_list.append(Card.score_single_card(card))

        if 'ace' in user_hand.cards and sum(scoring_list) < 11:
            scoring_list.append(10)

        hand_score = sum(scoring_list)

        return hand_score



def prompt_user_for_suit():
    """ask user for suit of card, return suit"""
    return input('\nWhat suit to use for card? ')

def prompt_user_for_rank():
    """ask user for rank, return rank"""
    return input('\nWhich card is it? ')

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
    print(user_hand)
    new_card = draw_new_card()
    user_hand.cards.append(new_card)
    print(user_hand)
    produce_final_score(user_hand)

    return 


def produce_final_score(user_hand):
    """returns total score of final hand"""
    
    score = user_hand.give_score()

    if score < 21:
        add_card_to_hand(user_hand)

    elif user_hand.give_score() == 21:
        print('winner, winner, chicken dinner!')
    
    else:
        print('wah, wah, wah...busted!')



def schematic():
    """functions that run the program, returns nothing"""
    # suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
    user_card1 = Card('cl', '9')  #format_single_card()
    user_card2 = Card('he', 'ace')  #format_single_card()
    user_hand = format_user_hand(user_card1, user_card2) 
    print(user_hand)
    
    #add_card_to_hand(user_hand)
    #print('second hand', user_card1, user_card2, user_hand)
    #user_hand = Hand([card1, card2])

    print(user_hand.give_score())

    produce_final_score(user_hand)


    

schematic()
