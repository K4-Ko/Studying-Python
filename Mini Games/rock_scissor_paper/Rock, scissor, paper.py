# Import required libraries
import random  # For generating random computer moves
from time import sleep  # For adding delays
import os  # For clearing the screen

# Define a list of possible moves, with index 0 empty for easier move selection
moves = ['', 'PAPER', 'ROCK', 'SCISSORS']

# Main game loop
while True:
    # Display game title with decorative borders using ANSI color codes
    # \033[1;31m = Red color
    # \033[1;32m = Green color
    # \033[m = Reset color
    print('\033[1;31m=-=\033[m'*20)
    print(' '*15,'\033[1;32mRock, Paper, Scissor\033[m')
    print('\033[1;31m=-=\033[m'*20)

    # Display move options in blue color
    print(' '*5,'\033[1;34mType (1) PAPER     (2) ROCK     (3) SCISSORS\033[m')

    # Get player's move (0 to exit)
    p = int(input('\n\033[1;32mEnter your choice (0 to exit):\033[m'))
    
    # Check if player wants to exit
    if p == 0:
        print('\033[1;31mGame over. See you next time!\033[m')
        break
    
    # Validate player's move
    if p < 0 or p > 3:
        print('\033[1;31mInvalid move! Try again.\033[m')
        continue
    
    # Generate computer's random move (1-3)
    pc = random.randint(1, 3)

    # Add suspense with a delay
    print('\033[1;32mThinking...\033[m')
    sleep(2)

    # Game logic to determine winner
    # Check for tie
    if p == pc:
        print('You both chose {}. It\'s a \033[1;34mTie\033[m!'.format(moves[p]))
    # Check all winning combinations for player
    elif p == 1 and pc == 2:  # Paper beats Rock
        print('You \033[1;32mWON\033[m because you chose {}, and I chose {}'.format(moves[p], moves[pc]))
    elif p == 2 and pc == 1:  # Rock loses to Paper
        print('You \033[1;31mLOST\033[m because you chose {}, and I chose {}'.format(moves[p], moves[pc]))
    elif p == 2 and pc == 3:  # Rock beats Scissors
        print('You \033[1;32mWON\033[m because you chose {}, and I chose {}'.format(moves[p], moves[pc]))
    elif p == 3 and pc == 2:  # Scissors loses to Rock
        print('You \033[1;31mLOST\033[m because you chose {}, and I chose {}'.format(moves[p], moves[pc]))
    elif p == 1 and pc == 3:  # Paper loses to Scissors
        print('You \033[1;31mLOST\033[m because you chose {}, and I chose {}'.format(moves[p], moves[pc]))
    elif p == 3 and pc == 1:  # Scissors beats Paper
        print('You \033[1;32mWON\033[m because you chose {}, and I chose {}'.format(moves[p], moves[pc]))
    
    # Wait for player to press Enter before starting next round
    print('\nPress Enter to play again...')
    input()
    
    # Clear the screen based on operating system
    # 'cls' for Windows (nt), 'clear' for Unix-based systems
    os.system('cls' if os.name == 'nt' else 'clear')
