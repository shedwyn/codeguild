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

for guessed_letter in secret_word:
    index = secret_word.find(guessed_letter,0)
    wrongly_guessed_letters.append[index]
    




def select_secret_word():
    """selects the secret word to use from the pre-set list.  returns word"""

    secret_word = 'DRAIN'
    return secret_word

#where index# in secret_word for guessed_letter in secret_word == 
    #index# in secret_word for guessed_letter in \
    #correctly_guessed_letters_string replace \
    #correctly_guessed_letters_string[index# of guessed_letter in secret_word]
    #with secret_word[index# of guessed_letter in secret_word]


if guessed_letter in secret_word:

    def update_correct_letters_string(
        guessed_letter, 
        secret_word, 
        wrongly_guessed_letters_list
        ):
        """take guessed letter return correctly_guessed_letters__string 
        or wrong letters list"""

        correct_index_number = secret_word.find(guessed_letter)
        while correct_index_number != -1
                #REPLACE 

        while correct_index_number != None
            
            if guessed_letter in secret_word:
                guessed_letter_index = secret_word[]

else:

    if guessed_letter not in secret_word:
        correct_index_number = None

def update_wrongly_guessed_letters(
    guessed_letter,
    wrongly_guessed_letters
    ):
    """takes in list and letter and adds letter to list
    returns the new list"""
    return wrongly_guessed_letters.append(guessed_letter)

        correct_index_number == None





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

def prompt_user_letter_guess():
    """asks the user to guess a letter.  returns user input"""
    return input('What letter would you like to guess?\n')

def check_user_guess():
    """takes in the user_letter_guess and """

    return ??

def update_letter_list():
    """takes in user_letter guess and assigns it to the correct list - 
    wrong or correct.  returns new list"""

    return new_list

###STRINGS HAVE A REPLACE FUNCTION### RETURN CORRECT GUESSES AS A STRING OF ITEMS SEPARATED BY A SPACE

secret_word_list = ['DRAIN', 'CLUB', 'APPLE', 'BEAR', 'ECHO', 'FARM', 'GOAT', 'HAZARD']

secret_word = select_secret_word()

#secret_word_letters_list = list(secret_word)

#correctly_guessed_letters = list(' __ ' * len(secret_word))

guessed_letters = {}
    #sub functions for wrong guesses and correct guesses
    #dict key1 = correct, dict key2 = incorrect
    #correct:[count of list of correct guesses], incorrect:[count of list \
    #of incorrect guesses]

correctly_guessed_letter_string = " ".join("__" * len(secret_word)) #stole 
    #from an actual hangman game previously presented.  would have done this
    #as a list of '__' instead and printed the list.

while guessed_letters['incorrect'] < 7

    user_letter_guess = prompt_user_letter_guess()

    print(correctly_guessed_letters)
    print(wrongly_guessed_letters)
    
    user_letter_guess = prompt_user_letter()

        if user_letter_guess in secret_word:
            for user_letter_guess in secret_word:
                replace





print


