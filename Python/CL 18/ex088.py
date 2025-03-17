# Create a program to help a lottery player generate guesses.  
# The program will ask how many games should be generated  
# and will randomly select 6 numbers between 1 and 60 for each game,  
# storing everything in a nested list.  

import random

lottery_number = []

n = int(input('How many games would you like to do: '))
c = 0
m = 0

# is the counter to generate the correcta amount of games, once the counter reaches the users input it will stop generating 
while c != n:
    c+=1
    print(f'The {c} game is: ',end='')
    # Generate a random number
    for g in range (0,6):
        m = random.randint(1, 60)
        # Check if the generate number is already in the list if it is, it will create a new number
        if m in lottery_number:
            while m in lottery_number:
                m = random.randint(1, 60)
        lottery_number.append(m)
        # Generate the line with 6 numbers and clean the lottery list to make a new one in the other line 
        if g == 5:
            print(f'{lottery_number}')
            lottery_number.clear()

        


