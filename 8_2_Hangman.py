#8_Hangman
#pick a secret word within code (hardwire - advanced use list?)
#show user blank spaces for every letter, unguessed 'Word: ' blank spaces for letters
#show user guessed letters for every letter they got correct 'WRONG = ' [list of letters guessed]
#show user previously guessed but incorrect letters
#let user enter new letter
#Let them guess until they get 6 letters wrong
#end correctly - "wrong" or "right" and reveal

#guessed letters (correct)
#incorrect guesses
#guesses remaining

#try writing out the bottom code before filling in the functions

def select_secret_word():
    """selects the secret word to use from the pre-set list.  returns word"""

    secret_word = 'DRAIN'
    return secret_word

def prompt_user_letter_guess():
    """asks the user to guess a letter.  returns user input"""
    guessed_letter = input('What letter would you like to guess?\n')
    return guessed_letter

def print_updated_score_board(
    correctly_guessed_letters, 
    wrongly_guessed_letters, 
    wrong_guesses_left,
    correct_letters_left
    ):
    """takes in all variables that belong to the scoreboard and prints"""
    
    # for items in letters_guessed:
    #     if items in list(secret_word):

    #     if items not in list(secret_word):

    print(
    'correct guesses:', correctly_guessed_letters, 
    '\nwrong guesses:', wrongly_guessed_letters, 
    '\nguesses remaining:', wrong_guesses_left,
    '\ncorrect letters left:', correct_letters_left
    )

def print_correct_guess_list(secret_word, all_guesses):
    """makes a list for secret word, tests guessed letters against, assigns as letter or dash
    and prints out the resulting string of letters or dashes"""
    secret_word_letters_list = list(secret_word)
    
    for letter in secret_word_letters_list:
        if letter not in all_guesses:
            secret_word.replace(letter, ' __ ')
    print(secret_word)

    # def create_wrong_guess_list(all_guesses, secret_word):
    #     """takes in guessed letters and secret_word.  returns list of wrong_guesses"""
   


def update_wrongly_guessed_letters(wrongly_guessed_letters, guessed_letter):
    print ("nope, not it!")
    wrongly_guessed_letters = wrongly_guessed_letters.add(guessed_letter)
    return wrongly_guessed_letters

def update_correctly_guessed_letters(correctly_guessed_letters, guessed_letter):
    print ('yes!')
    correctly_guessed_letters = correctly_guessed_letters.add(guessed_letter)
    return correctly_guessed_letters
    
#print_correct_guess_list('DRAIN', ['A', 'B', 'D', 'H'])

# play_prompt = input('Would you like to play hangman?  Yes or No: ').upper

# if play_prompt == 'YES':
    
#secret_word_list = ['DRAIN', 'CLUB', 'APPLE', 'BEAR', 'ECHO', 'FARM', 'GOAT', 'HAZARD']

secret_word = select_secret_word()

correctly_guessed_letters = set()

wrongly_guessed_letters = set()

wrong_guesses_left = 6

correct_letters_left = len(secret_word) - len(correctly_guessed_letters)

while wrong_guesses_left > 0 and correct_letters_left > 0:

    guessed_letter = prompt_user_letter_guess().upper()

    if guessed_letter in list(secret_word):
        update_correctly_guessed_letters(correctly_guessed_letters, 
            guessed_letter)
        correct_letters_left = len(secret_word) - len(correctly_guessed_letters)

    else:
        update_wrongly_guessed_letters(wrongly_guessed_letters, guessed_letter)
        wrong_guesses_left -= 1
        
    
    print_updated_score_board(correctly_guessed_letters, 
        wrongly_guessed_letters, wrong_guesses_left, correct_letters_left)
        

print("-*" * 10)
print('The word was', secret_word)
print ('Game Over')

#print ('Goodbye')


        




    #sub functions for wrong guesses and correct guesses
    #dict key1 = correct, dict key2 = incorrect
    #correct:[count of list of correct guesses], incorrect:[count of list \
    #of incorrect guesses]

#correctly_guessed_letters = " ".join("__" * len(secret_word)) #stole 
    #from an actual hangman game previously presented.  would have done this
    #as a list of '__' instead and printed the list.

# while guessed_letters['incorrect'] < 7

#     user_letter_guess = prompt_user_letter_guess()

#     print(correctly_guessed_letters)
#     print(wrongly_guessed_letters)
    
#     user_letter_guess = prompt_user_letter()

#         if user_letter_guess in secret_word:
#             for user_letter_guess in secret_word:
#                 replace



#where index# in secret_word for guessed_letter in secret_word == 
    #index# in secret_word for guessed_letter in \
    #correctly_guessed_letters_string replace \
    #correctly_guessed_letters_string[index# of guessed_letter in secret_word]
    #with secret_word[index# of guessed_letter in secret_word]


# if guessed_letter in secret_word:

#     def update_correct_letters_string(
#         guessed_letter, 
#         secret_word, 
#         wrongly_guessed_letters_list
#         ):
#         """take guessed letter return correctly_guessed_letters__string 
#         or wrong letters list"""

#         correct_index_number = secret_word.find(guessed_letter)
#         while correct_index_number != -1
#                 #REPLACE 

#         while correct_index_number != None
            
#             if guessed_letter in secret_word:
#                 guessed_letter_index = secret_word[]

# else:

#     if guessed_letter not in secret_word:
#         correct_index_number = None

# def update_wrongly_guessed_letters(
#     guessed_letter,
#     wrongly_guessed_letters
#     ):
#     """takes in list and letter and adds letter to list
#     returns the new list"""
#     return wrongly_guessed_letters.append(guessed_letter)

#         correct_index_number == None





#I need to take the letter given
#find out if it is in the secret word
#if it is:
    #find the index #s in secret word \
    #find where that letter resides in secret word (funciton that takes \
        #in secrete word and guess and ret)
    #replace the __ in the correct guess string at that/those indices
#if it is not:
    #place the incorrect guess in the incorrect guess list and \
    #add that wrong guess to the tally of wrong guesses (on 6th wrong \
        #- end game)
#end game when word is guessed or user has guessed 6 times\
    #whichever comes first


# def check_user_guess():
#     """takes in the user_letter_guess and """

#     return ??

# def update_letter_list():
#     """takes in user_letter guess and assigns it to the correct list - 
#     wrong or correct.  returns new list"""

#     return new_list

###STRINGS HAVE A REPLACE FUNCTION### RETURN CORRECT GUESSES AS A STRING OF ITEMS SEPARATED BY A SPACE


