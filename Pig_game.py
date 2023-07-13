import random
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

# Create a roll() function
def roll():
    min_value = 1
    max_value = 6
    rolled = random.randint(min_value,max_value)
    return rolled

# Set game max score and set initial scores
max_score = 50

# Instructions
print(f'\n*********************************************************'\
      f'\n**            {Fore.GREEN}Welcome to my Pig game!{Style.RESET_ALL}                  **'\
      f'\n** The goal of this game is to be the highest scoring  **'\
      f'\n** player with a score over {max_score}.  Each round the player **'\
      f'\n** has an opportunity to add to their total score by   **'\
      f'\n** rolling a die.  However, if they roll a 1, they end **'\
      f'\n** the round with a score of 0.                        **'\
      f'\n**                   {Fore.YELLOW}GOOD LUCK!{Style.RESET_ALL}                        **'\
      f'\n*********************************************************\n\n')  

# Have the user select how many players (2-4)
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2<= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")    

# Create roll_decision function to get user decision and return current_roll value
def roll_decision():
    while True:
        continue_roll = input("Would you like to roll (y/n)? ")
        if continue_roll.lower() == "y" or continue_roll.lower() == "n":
            if continue_roll.lower() == "y":
                current_roll = roll()
                return current_roll
            return 0
        else:
            print("Please select y or n.")

# Set initial scores
player_scores = [0 for _ in range(players)]

# Play game until player reaches max_score
while max(player_scores) < max_score:
    for player_idx in range(players):
        print(f'{Fore.BLUE}\nPlayer {player_idx +1} turn has just started!')
        print(f'Your current total score is: {player_scores[player_idx]}\n{Style.RESET_ALL}')
        current_score = 0
        while True:
            value = roll_decision()
            if value != 0:
                if value == 1:
                    print(f'{Fore.RED}You rolled a 1! You loose all points for this round.{Style.RESET_ALL}')
                    current_score = 0
                    break
                else:
                    current_score += value
                    print(f'You rolled a: {Fore.YELLOW}{value}{Style.RESET_ALL}')
                print(f'Your score is: {Fore.YELLOW}{current_score}{Style.RESET_ALL}')
            else:
                break
        player_scores[player_idx] += current_score
        print(f'{Fore.MAGENTA}Your total score is: {player_scores[player_idx]}{Style.RESET_ALL}')

# Declare winner
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(f'\n{Fore.GREEN}Player number {winning_idx +1} is the winner with a score of {max_score}{Style.RESET_ALL}\n\n')
