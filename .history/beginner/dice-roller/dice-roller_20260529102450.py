import random

print("\tWelcome to the Dice game\n")

def Menu():
    print(input("How many players will be playing?: "))

def RollDice():
    roll = random.randint(1, 6)
    return roll


Menu()
print(RollDice())