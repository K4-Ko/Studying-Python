# Create a program to manage a soccer player's performance. 
# The program will read the player's name and the number of matches played. 
# Then, it will read the number of goals scored in each match. 
# In the end, all this data will be stored in a dictionary, 
# including the total number of goals scored during the championship.

player_list = {}

player_list['name'] = str(input("Player's name: "))
player_list['matches'] = int(input('How many matches?: '))
g = []

for c in range (0, player_list['matches']):
    g.append (int(input(f'How many goals did he score in the {c} match: ')))
    player_list['goals'] = g [:]

player_list['total'] = sum(g)

print('=-='*10)

print(f'\nThe players name is: {player_list['name']} \nThe player has played: {player_list['matches']} matches')
print(f'The amount of goals per match: {player_list["goals"]} \nThe total amount is: {player_list['total']}')

print('=-='*10)

print(f'The player: {player_list['name']} has played {player_list['matches']}: ')

for m, goals in enumerate(player_list['goals']):
    print(f'{' '*5} => In the macth {m} {player_list['name']} Scored : {goals} goals')
print(f'The total amout of goals is: {player_list['total']}')