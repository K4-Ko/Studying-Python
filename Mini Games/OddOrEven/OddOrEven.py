# Game: Odd or Even against computer
# The program continues until player loses and shows total consecutive victories

import random  # Import random module to generate computer's number

c = 0  # Counter for consecutive victories

while True:  # Infinite loop until player loses
    # Player inputs a number between 1-10
    n = int(input('Type a number from 1 to 10: '))
    
    # Computer randomly chooses a number between 1-10
    pc = random.randint(1,10)
    
    # Player chooses Odd or Even (takes first letter only)
    p = str(input('Odd or Even? [O] odd [E]: ')).upper().strip()[0]

    # Calculate sum of player's and computer's numbers
    s = pc + n

    # Check if sum is even AND player chose Even
    if s % 2 == 0 and p =='E':
        print(f'You won, I choose {pc} !')
        c+= 1  # Increment victory counter
        
    # Check if sum is odd AND player chose Odd
    if s % 2 != 0 and p =='O':
        print(f'You won, I choose {pc} !')
        c+= 1  # Increment victory counter
        
    # Check losing conditions: 
    # (sum is even but player chose Odd) OR (sum is odd but player chose Even)
    if s % 2 == 0 and p =='O' or s % 2 != 0 and p =='E':
        print(f'You Lost, I choose {pc}!')
        if c > 0:  # If player had any victories
            print(f'You won {c} in a row !')
        break  # End the game