import random

#Guess Number
#gen ran num 1, 100
#user guesses
#comp output of guess high or low
#once guess is correct, quit


def gen_secret_num():
    """generate a random number between 1 and 50. Return it"""
    return random.randint(1, 50)

def prompt_user_to_guess():
    """prompt user to guess a number between 1 and 50.  Return it as an integer."""
    return int(input("Guess a number between 1 and 50: "))

def determine_if_guess_correct_or_no(secret_num, ran_num):
    """determines if the user guess is too high or low or correct.  Print message for user."""
    if guess_num > ran_num:
        print('too high, go lower')
    elif guess_num < ran_num:
        print('too low, go higher')

def guess_game_run_loop():
    print('let\'s play a game, i will pick a number between 1 ' +
    'and 50, and then you will try to guess it')
    ran_num = gen_secret_num()
    guess_num = prompt_user_to_guess()
    while guess_num != ran_num:
        determine_if_guess_correct_or_no(guess_num, ran_num)
    print ('You got it!')

guess_game_run_loop()


#guess_num = int(input("guess a number between 1 and 100: "))

#is there a way to make this more concise and not \
#repeat myself as often? may require rewriting the \
#loop
#gold prize using input only once
#another version would limit the number of guesses \
#and would need to minimize the random spread