import random

print("\tWelcome to the Dice game\n")

def Menu():
    playercount = input("How many players will be playing?: ")
    print("playercount, ", playercount)



def RollDice():
    roll = random.randint(1, 6)
    return roll


Menu()
# print(RollDice())