import random 
from time import sleep

# LIST OF MOVES:
moves = ['', 'PAPER', 'ROCK', 'SCISSORS']

print('\033[1;31m=-=\033[m'*20)
print(' '*25,'\033[1;32mRock, Paper, Scissors\033[m')
print('\033[1;31m=-=\033[m'*20)

print(' '*5,'\033[1;34mEnter (1) PAPER     (2) ROCK     (3) SCISSORS\033[m')

p = int(input('\n\033[1;32mEnter your choice:\033[m '))
pc = random.randint(1, 3)

print('\033[1;32mThinking...\033[m')
sleep(2)

if p == pc:
    print('You both chose {}. It\'s a \033[1;34mDraw\033[m!'.format(moves[p]))
elif p == 1 and pc == 2:
    print('You \033[1;32mWon\033[m! You chose {}, and I chose {}'.format(moves[p], moves[pc]))
elif p == 2 and pc == 1:
    print('You \033[1;31mLost\033[m! You chose {}, and I chose {}'.format(moves[p], moves[pc]))
elif p == 2 and pc == 3:
    print('You \033[1;32mWon\033[m! You chose {}, and I chose {}'.format(moves[p], moves[pc]))
elif p == 3 and pc == 2:
    print('You \033[1;31mLost\033[m! You chose {}, and I chose {}'.format(moves[p], moves[pc]))
elif p == 1 and pc == 3:
    print('You \033[1;32mWon\033[m! You chose {}, and I chose {}'.format(moves[p], moves[pc]))
elif p == 3 and pc == 1:
    print('You \033[1;31mLost\033[m! You chose {}, and I chose {}'.format(moves[p], moves[pc]))
