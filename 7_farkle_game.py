#7_farkle_game

# roll 5 6-sided dice
# score all 5
# may want to name the dice
# 3 x 1 = 1000
# 3 x 2:7 = 200
# 1 x 1 - 100
# 1 x 5 - 50
# no score = 'farkle, you loser!'

#Advanced
#re-roll any dice
#save scoring dice aside and roll only losing dice \
    #if win something.  if re-roll wins, add to total of \
    #"that" roll- roll losing die again and add winning

import random

print('Let\'s play Farkle!')

def roll_function():
    """"roll die.  return value""""

def store_roll_scores(value):
    """take in value from roll_function and move to \
    list or dict record.  return appended list or dict"""

def determine_roll_points_earned(value_list):



number_of_dice = 5
number_of_rolls = 0
results_list = []


#name 5 dice
#roll - roll random 5 times and add to a list?
    #or roll 5 times and add each to a variable?

#calc if we have 3 matching results - get point score
    #calc if any of the remaing 2 results score points
#calc if no 3 match, if any dice match - get point score
#return "farkle!" if no dice score 
#ask if you want to play again

while number_of_rolls < 6:
	roll_the_dice = random.randint(1, 6)
	results_list.append(roll_the_dice)
	number_of_rolls += 1

results_list.sort()

print(results_list)