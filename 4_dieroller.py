#Die Roller
#Ask user # of 6-sided dies:
#Roll and print
#Print sum all dies
import random

def user_input_die_number():
    """"ask user how many dice s/he wants to roll. Return as integer."""
    return int(input('How many dice would you like to roll? '))

def roll_6_side_dice():
    """roll a 6 sided die.  return value."""
    return random.randint(1, 6)

def sum_tally_roll_values(list_of_values):
    """adds up all the values on a list.  Returns sum."""
    return sum(list_of_values)

def record_roll_values(roll_values):
    dice_roll = roll_6_side_dice()
    roll_values.append(dice_roll)
    return roll_values

number_of_rolls = user_input_die_number()
roll_count = 0
roll_values = []

while roll_count != number_of_rolls:
    roll_values = record_roll_values(roll_values)
    roll_count += 1

tally_of_dice = sum_tally_roll_values(roll_values)

average_of_rolls = tally_of_dice/number_of_rolls

print('\nYou rolled ' + str(roll_count) + ' times',\
    '\n\nHere is the list of your rolls:', roll_values, \
    '\n\nThe total value of the rolls was:', tally_of_dice, \
    '\n\nThe average value of your rolls was:', average_of_rolls)
