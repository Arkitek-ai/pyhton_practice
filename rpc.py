import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0
    tie_game = 0
    def play_rps():
        class RPS(Enum):
            Rock = 1
            Paper = 2
            Scissors = 3
        
        player_choice = input("\nEnter...\n1 for Rock\n2 for Paper\n3 for Scissors\n\n")
        if player_choice not in ["1","2","3"]:
            print("You must enter 1, 2 or 3.")
            return play_rps()
        player = int(player_choice)
        computer_choice = random.choice("123")
        computer = int(computer_choice)

        def decide_winner(player, computer):
            if player == 1 and computer == 3:
                nonlocal player_wins
                player_wins += 1
                return "🥳 You Win!"
            elif player == 1 and computer == 2:
                # nonlocal player_wins
                player_wins += 1
            elif player == 3 and computer == 2:
                # nonlocal player_wins
                player_wins += 1
                return "🥳 You Win!"
            elif player == computer:
                nonlocal tie_game
                tie_game += 1
                return "😲 Tie Game!"
            else:
                nonlocal python_wins
                python_wins += 1
                return "🐍 Python Wins"
            nonlocal game_count
            game_count += 1
        winner = decide_winner(player, computer)
        print(winner)

        print("\nYou Chose " + str(RPS(player)).replace("RPS.", ""))
        print("\nPython Chose " + str(RPS(computer)).replace("RPS.", ""))
 
        print("\nPlay Again?")
        while True:
            play_again = input("\nY for Yes or\nQ for Quit\n\n")
            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break

        if play_again.lower() == "y":
            return rps()
        else:
            print("\n🎇🎇🎇")
            print("\nThank You For Playing!")
            sys.exit("\n👋👋👋")
    play_rps()
rps()
