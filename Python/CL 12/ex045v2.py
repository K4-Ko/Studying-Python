import random 
from time import sleep
import os 

# LIST OF MOVES:
moves = ['', 'PAPER', 'ROCK', 'SCISSORS']

while True:
    print('\033[1;31m=-=\033[m'*20)
    print(' '*25,'\033[1;32mRock, Paper, Scissors\033[m')
    print('\033[1;31m=-=\033[m'*20)

    print(' '*5,'\033[1;34mType (1) PAPER     (2) ROCK     (3) SCISSORS\033[m')

    p = int(input('\n\033[1;32mEnter your choice (0 to exit):\033[m'))
    
    if p == 0:
        print('\033[1;31mGame over. See you next time!\033[m')
        break
        
    if p < 0 or p > 3:
        print('\033[1;31mInvalid move! Try again.\033[m')
        continue
        
    pc = random.randint(1, 3)

    print('\033[1;32mThinking...\033[m')
    sleep(2)

    if p == pc:
        print('You both chose {}. It\'s a \033[1;34mTie\033[m!'.format(moves[p]))
    elif p == 1 and pc == 2:
        print('You \033[1;32mWON\033[m because you chose {}, and I chose {}'.format(moves[p], moves[pc]))
    elif p == 2 and pc == 1:
        print('You \033[1;31mLOST\033[m because you chose {}, and I chose {}'.format(moves[p], moves[pc]))
    elif p == 2 and pc == 3:
        print('You \033[1;32mWON\033[m because you chose {}, and I chose {}'.format(moves[p], moves[pc]))
    elif p == 3 and pc == 2:
        print('You \033[1;31mLOST\033[m because you chose {}, and I chose {}'.format(moves[p], moves[pc]))
    elif p == 1 and pc == 3:
        print('You \033[1;31mLOST\033[m because you chose {}, and I chose {}'.format(moves[p], moves[pc]))
    elif p == 3 and pc == 1:
        print('You \033[1;32mWON\033[m because you chose {}, and I chose {}'.format(moves[p], moves[pc]))
    
    print('\nPress Enter to play again...')
    input()
    
    os.system('cls' if os.name == 'nt' else 'clear')
