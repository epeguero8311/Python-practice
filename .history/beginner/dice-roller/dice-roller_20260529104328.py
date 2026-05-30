import random
import time

print("\tWelcome to the Dice game\n")

players = {}

def Menu():
    playercount = int(input("How many players will be participating? (Minimum: 2): "))
    
    for i in range(1, playercount + 1):
        players[i] = f"Player {i}"

    for player_id, player in players.items():
        # print(f"{player_id}: {player}")
        print("Press Enter to roll")
        user_respones = input(print(f"{player}'s turn: "))

        if user_respones == "":
            print("Rolling...")
            time.sleep(2)
            



def RollDice():
    roll = random.randint(1, 6)
    return roll


Menu()
# print(RollDice())