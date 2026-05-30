import random

print("\tWelcome to the Dice game\n")

def RollDice():
    roll = random.randint(1, 6)
    print(roll)

RollDice()