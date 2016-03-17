#Die Roller
#Ask user # of 6-sided dies:
#Roll and print
#Print sum all dies
import random

num_rolls = 0
num_dice = int(input('how many dice '))
sum_dice = 0

while num_rolls < num_dice:
    dice_roll = random.randint(1,6)
    print('roll value:', dice_roll)
    sum_dice += dice_roll
    num_rolls += 1

print('the die sum =', sum_dice, 'the average is', sum_dice/num_dice)