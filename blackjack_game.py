import random


class Card:
    suits = ['clubs', 'spades', 'hearts', 'diamonds']
    ranks = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']

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


class Deck:
    def __init__(self, cards):
        """takes in self and list of cards"""
        self.cards = cards
        random.shuffle(self.cards)

    def __repr__(self, cards):
        return 'Deck({})'.format(self.cards)

    def deal_card(self):
        """takes in nothing.  deals 2 cards to player and to dealer"""
        card = self.cards.pop()
        return card

    # def deal_hand(self):
    #     """takes in nothing.  deals 2 cards to player and to dealer"""
    #     random.shuffle(self.cards)
    #     card1 = self.cards.pop()
    #     card2 = self.cards.pop()
    #     hand = Hand([card1, card2])
    #     print('\n\n Your hand:  ', hand)
    #     return hand


def prompt_user_for_suit():
    """ask user for suit of card, return suit"""
    return input('\nWhat suit to use for card? ')

def prompt_user_for_rank():
    """ask user for rank, return rank"""
    return input('\nWhich card is it? ')

def create_deck():#look at product() for this
    """takes nothing, instantiates Card for single cards and instantiates
    Deck.  returns deck dictionary"""
    suits = ['clubs', 'spades', 'hearts', 'diamonds']
    ranks = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
    deck_dict = {}
    deck_list = []
    for suit in suits:
        card_suit = suit
        for rank in ranks:
            card_rank = rank
            card_name = '{} | {}'.format(card_suit, card_rank)
            single_card = format_single_card(suit, rank)  #rmv later
            deck_dict[card_name] = single_card  #rmv later
            deck_list.append(single_card)
    deck_cards = Deck(deck_list)
    return deck_cards

def format_single_card(suit, rank):
    """takes in suit & rank, prompts for card variables, returns instantiated card"""
    return Card(suit, rank)

def draw_new_card():
    """takes nothing, creates new card, returns updated hand"""
    new_card = deal_card(self)
    #return 

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
        draw_answer = input('\nDraw again (D) or Hold (H):  ')
        print('\n')
        if draw_answer == 'D':
            deal_card(self)
        else:
            print('no draw')
        add_card_to_hand(user_hand)
    elif user_hand.calc_hand_score() == 21:
        print('winner, winner, chicken dinner!')   
    else:
        print('wah, wah, wah...busted!')

def main():
    """functions that run the program, returns nothing"""
    deck_cards = create_deck()
    player_hand = Hand([deck_cards.deal_card(), deck_cards.deal_card()])
    print(player_hand)
    computer_hand = Hand([deck_cards.deal_card(), deck_cards.deal_card()])


    produce_final_score(player_hand)





    # user_card1 = format_single_card()
    # user_card2 = format_single_card()
    # user_hand = format_user_hand(user_card1, user_card2) 
    # produce_final_score(user_hand)
    # hand = Hand([Card('cl', '2'), Card('cl', 'ace')])
    # produce_final_score(hand)


main()
