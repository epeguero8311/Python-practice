import random
import time

print("\tWelcome to the Dice game\n")

players = {}

def Menu():
    playercount = int(input("How many players will be participating? (Minimum: 2): "))
    
    for i in range(1, playercount + 1):
        players[i] = f"Player {i}"

    for player_id, player in players.items():
        while True:
            user_response = input(f"\n{player['name']}'s turn - Press Enter to roll: ")

            if user_response == "":
                print("Rolling...")
                time.sleep(2)

                roll = RollDice()
                print(roll)

                players[player_id]["roll"] = roll

                break
            else:
                print("Please ONLY press Enter.")
                
    LeaderBoard()


def LeaderBoard():
    return print("\tLEADERBOARD\n")

def RollDice():
    roll = random.randint(1, 6)
    return roll


Menu()
# print(RollDice())