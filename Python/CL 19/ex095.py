# Improve challenge 93 so that it works with multiple players, 
# including a system to view detailed performance information for each player.

player= {}
goals = []
team = []
c = 0

while True:
    print('---'*20)
    goals.clear()
    c+=1
    player['code'] = c
    player['name'] = str(input("Player's name: "))
    player['matches'] = int(input(f'How many matches has {player['name']} played ?: '))
    
    for c in range (0, player['matches']):
        # goals.append(int(input(f'How many goals {player['name']} scored in the {c} match ?: ')))
        # player['goals'] = goals
        goals_made = int(input(f'How many goals {player['name']} scored in the {c} match ?: '))
        goals.append(goals_made)
        player['goals'] = (goals[:])

    while True:
        q = str(input('Would you like to continue [Y] to continue or [N] to stop: ')).upper().split()[0]
        if q in 'YN':
            break
        print('Try again!')
    
    team.append(player.copy())
    
    if q == 'Y':
        continue
    elif q == 'N':
        print('=-='*20)
        break

#===================================================================================================================

print('-' * 60)
print(f'{"Code":<5}{"Name":<15}{"Goals":<25}{"Total":>5}')
print('-' * 60)

for player in team:
    print(f'{player["code"]:<5}{player["name"]:<15}{str(player["goals"]):<25}{sum(player["goals"]):>5}')


print(team)

