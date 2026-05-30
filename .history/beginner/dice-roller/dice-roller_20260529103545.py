import random

print("\tWelcome to the Dice game\n")

players = {}

def Menu():
    playercount = int(input("How many players will be participating? (Minimum: 2): "))
    
    for i in range(1, playercount + 1):
        players[i] = f"Player {i}"

    print(players)



def RollDice():
    roll = random.randint(1, 6)
    return roll


Menu()
# print(RollDice())