# Create a program where 4 players roll a die and get random results. 
# Store these results in a dictionary in Python. 
# In the end, sort this dictionary, knowing that the winner is the one who rolled the highest number.
from time import sleep
from random import randint

player_stat = {}

for x in range (1,6): 
    player_stat [f'Player {x}'] = randint(1,6)
    
print ('Those are the results:')

for player, score in player_stat.items():
    print(f'{player} got the number: {score}')
    sleep(1)

s = dict(sorted(player_stat.items(), key = lambda item: item[1], reverse = True)) 

print('==========Ranking==========')

for player, score in s.items():
    print(f'{player} got the number: {score}')
    sleep(1)
