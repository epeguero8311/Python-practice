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
        user_respones = input(f"{player}'s turn: ")

        while True:
            user_response = input(f"\n{player}'s turn - Press Enter to roll: ")

            if user_response == "":
                print("Rolling...")
                time.sleep(2)
                print("67")
                break
            else:
                print("Please ONLY press Enter.")



def RollDice():
    roll = random.randint(1, 6)
    return roll


Menu()
# print(RollDice())