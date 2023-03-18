"""
This is a Dice Roller
"""

import random


user_input = input("Enter Y to roll the dice, or enter N to stop the program : ").capitalize()

dice_number = None

if user_input == 'Y':
    dice_number = random.randint(1, 6)

print("Dice is : ")

if dice_number == 1:
    print("_ _ _")
    print("     ")
    print("  *  ")
    print("     ")
    print("_ _ _")

elif dice_number == 2:
    print("_ _ _")
    print("     ")
    print("*   *")
    print("     ")
    print("_ _ _")

elif dice_number == 3:
    print("_ _ _")
    print("*    ")
    print("  *  ")
    print("    *")
    print("_ _ _")


elif dice_number == 4:
    print("_ _ _")
    print("*   *")
    print("     ")
    print("*   *")
    print("_ _ _")


elif dice_number == 5:
    print("_ _ _")
    print("*   *")
    print("  *  ")
    print("*   *")
    print("_ _ _")


elif dice_number == 6:
    print("_ _ _")
    print("*   *")
    print("*   *")
    print("*   *")
    print("_ _ _")



