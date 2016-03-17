import random

#Guess Number
#gen ran num 1, 100
#user guesses
#comp output of guess high or low
#once guess is correct, quit

print('let\'s play a game, i will pick a number between 1 ' +
    'and 100, and then you will try to guess it')

ran_num = random.randint(1, 100)
guess_num = 0

#guess_num = int(input("guess a number between 1 and 100: "))

while guess_num != ran_num:
    guess_num = int(input("guess a number between 1 and 100: "))
    if guess_num > ran_num:
        print('too high, go lower')
    elif guess_num < ran_num:
        print('too low, go higher')
    else:
        print('you got it!')




#is there a way to make this more concise and not \
#repeat myself as often? may require rewriting the \
#loop
#gold prize using input only once
#another version would limit the number of guesses \
#and would need to minimize the random spread