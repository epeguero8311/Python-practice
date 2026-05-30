import random
import time

print("\tWelcome to the Dice Game\n")

players = {}

def Menu():
    while True:
        playercount = int(input("How many players will be participating? (Minimum: 2): "))

        if playercount >= 2:
            break

        print("You must have at least 2 players.\n")

    for i in range(1, playercount + 1):
        players[i] = {
            "name": f"Player {i}",
            "roll": None
        }

    for player_id, player in players.items():
        while True:
            user_response = input(
                f"\n{player['name']}'s turn - Press Enter to roll: "
            )

            if user_response == "":
                print("Rolling...")
                time.sleep(2)

                roll = RollDice()
                print(f"{player['name']} rolled a {roll}")

                players[player_id]["roll"] = roll
                break
            else:
                print("Please ONLY press Enter.")

    LeaderBoard()


def LeaderBoard():
    print("\n\tLEADERBOARD\n")

    sorted_players = sorted(
        players.values(),
        key=lambda player: player["roll"],
        reverse=True
    )

    for place, player in enumerate(sorted_players, start=1):
        print(f"{place}. {player['name']} - {player['roll']}")

    winner = sorted_players[0]
    print(f"\nWinner: {winner['name']} with a roll of {winner['roll']}")


def RollDice():
    return random.randint(1, 6)


Menu()