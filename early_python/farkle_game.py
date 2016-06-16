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

class Dice:
    def __init__(self, result):
        self.result = result


def roll_dice():
    return random.randint(1, 6)

def roll_5_dice():
    return sorted([roll_dice() for _ in range(1, 6)])

def score_points(single_count):
    if single_count == 3:
        points = points + 1000
    elif dice_result.count(2) == 3 or
        dice_result.count(3) or
        dice_result.count(4) or
        dice_result.count(5) or
        dice_result.count(6):
        points = points + 200
    elif dice_result.count(3)
    

def figure_counts(dice_result):
    return number_to_count = {
        1:dice_result.count(1),
        2:dice_result.count(2),
        3:dice_result.count(3),
        4:dice_result.count(4),
        5:dice_result.count(5),
        6:dice_result.count(6)
        }
    
    for _ in list_of_rolls:
        count(1)
while counter <= len(dice_result_list)
    number_to_count = figure_counts(dice_result)
    for _ in figure_counts:
        if over_3_type(figures_counts[1]) == True and over_3_type is count(1):
            score += 1000
        elif over_3_type(fi)



def over_3_type(dice_result):
    return dice_result >3


    if number_to_count[1] > 3:
        return points[1] > 3

    if 
    


    for _ in figure_counts




def match_dice():
    dice_result = roll_5_dice()
    figure_counts(dice_result)

    print()

def main():
    match_dice()

main()




# print('Let\'s play Farkle!')

# def roll_function():
#     """roll die.  return value"""

#     return value

# def store_roll_scores(value):
#     """take in value from roll_function and move to \
#     list or dict record.  return appended list or dict"""

# def determine_roll_points_earned(value_list):



# number_of_dice = 5
# number_of_rolls = 0
# results_list = []


# #name 5 dice
# #roll - roll random 5 times and add to a list?
#     #or roll 5 times and add each to a variable?

# #calc if we have 3 matching results - get point score
#     #calc if any of the remaing 2 results score points
# #calc if no 3 match, if any dice match - get point score
# #return "farkle!" if no dice score 
# #ask if you want to play again

# while number_of_rolls < 6:
# 	roll_the_dice = random.randint(1, 6)
# 	results_list.append(roll_the_dice)
# 	number_of_rolls += 1

# results_list.sort()

# print(results_list)