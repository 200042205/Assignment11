# put your dice_roll() function in this file
import random

def dice_function(dice_type):
    dice_range = range(1, dice_type+1)
    value = random.choice(dice_range)
    return str(value)