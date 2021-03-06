import textwrap
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
        print('calc_hand_score = ', self.cards)
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

    def add_card_to_hand(self, deck_cards):
        """takes new card and hand, adds card to hand, returns new_hand"""
        #deck_cards = deck_cards
        new_card = deck_cards.deal_card()
        new_hand = self.cards.append(new_card) # .append does not return anything
            #, it appends and moves on

        return new_hand

    # def decide_player_draw_or_hold(player_hand, deck_cards):
    #     draw_answer = input('\nDraw again (D) or Hold (H):  ')
    #     print('\n')
    #     if draw_answer == 'D':
    #         user_hand.add_card_to_hand(deck_cards)
    #     else:
    #         print('\n No draw, Human entity holds')
    #     return player_hand


class Deck:
    def __init__(self, cards):
        """takes in self and list of cards"""
        self.cards = cards
        random.shuffle(self.cards)

    def __repr__(self, cards):
        return 'Deck({})'.format(self.cards)

    def deal_card(self):
        """takes in nothing.  deals card, returns card"""
        return self.cards.pop()

    
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

def format_single_hand(hand_list):
    """take in list and instatiates into Hand, returns instatiated hand"""
    return Hand(hand_list)

def deal_more_cards(user_hand, computer_hand, deck_cards):
    """takes in scores, hands, deck.  continues dealing until win or bust.  returns??"""
    player_score = user_hand.calc_hand_score()
    computer_score = computer_hand.calc_hand_score()
    print(user_hand, computer_hand)
    if player_score < 21 and computer_score < 21:
        # user_hand.decide_player_draw_or_hold(deck_cards)   
        draw_answer = input('\nDraw again (D) or Hold (H):  ')
        print('\n')
        if draw_answer == 'D':
            player_hand = user_hand.add_card_to_hand(deck_cards)
            print('You are now holding these cards:  ', player_hand)
        else:
            print('\n No draw, Human entity holds')  
    elif player_score < 21 and computer_score < 17:
        print('\nComputer entity must draw')
        computer_hand = computer_hand.add_card_to_hand(deck_cards)
        print('You are now holding these cards:  ', computer_hand)
    return determine_winner(player_hand, computer_hand, deck_cards)
    
def determine_winner(user_hand, computer_hand, deck_cards):
    """takes in hands, deck, uses if statements to determine 
    winner, returns win statement"""
    computer_win = textwrap.wrap('HAL wins!  Please report to the airlock immediately for ejection.', 40)
    player_win = textwrap.wrap('Player wins this round!  The computer let you win, you know that, right?', 40)
    tie_win = textwrap.wrap('Unbelievable!  A tie!  We should play best 2 out of 3!', 40)
    tie_loss = textwrap.wrap('Unbelievable!  A tie loss!  How did that happen?!', 40)
    print(user_hand)
    player_score = user_hand.calc_hand_score()
    print(computer_hand)
    computer_score = computer_hand.calc_hand_score()
    game_answer = 'empty line'
    print(
        '\nplayerscore', player_score,
        '\ncomputerscore', computer_score, 
        '\nuser_hand', user_hand,
        '\ncomputer_hand', computer_hand
    )
    if player_score == 21 and computer_score < 21:
        game_answer = player_win
    elif player_score < 21 and computer_score == 21:
        game_answer = computer_win
    elif player_score == 21 and computer_score == 21:
        game_answer = tie_win
    elif player_score > 21 and computer_score > 21:
        game_answer = tie_loss
    # elif player_score < 21 and computer_score < 21:
    #     if player_score > computer_score:
    #         game_answer = player_win
    #     else:
    #         game_answer = computer_win
    else:
        deal_more_cards(user_hand, computer_hand, deck_cards)
    return game_answer

def play_game(deck_cards):
    """game play function, returns None"""
    #deck_cards = deck_cards 
    player_hand = format_single_hand([deck_cards.deal_card(), deck_cards.deal_card()])
    computer_hand = format_single_hand([deck_cards.deal_card(), deck_cards.deal_card()])
    player_score = player_hand.calc_hand_score()
    computer_score = computer_hand.calc_hand_score()
    print('\nPlayer\'s initial score is:  ', player_score)
    print('\nComputer\'s initial score is:  ', computer_score)
    print(
        '\n',
        determine_winner(player_hand, computer_hand, deck_cards)
    )
    return None

def main():
    """functions that run the program, returns nothing"""
    deck_cards = create_deck()
    play_game(deck_cards)
    print('\nWould you like to play another game?')
    play_again = input('\n  Y or N?  ')
    if play_again == 'Y':
        main()
    else:
        print('\n Goodbye, human.')

   
main()