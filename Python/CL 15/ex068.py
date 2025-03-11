# Create a program that plays odd or even with the computer. 
# 
# The game will stop only when the player loses, showing the total number of consecutive victories they achieved at the end of the game

import random

c = 0 

while True:
    n = int(input('Type a number from 1 to 10: '))
    pc = random.randint(1,10)
    p = str(input('Odd or Even? [O] odd [E]: ')).upper().strip()[0]

    s = pc + n

    if s % 2 == 0 and p =='E':
        print(f'You won, I choose {pc} !')
        c+= 1
        
    if s % 2 != 0 and p =='O':
        print(f'You won, I choose {pc} !')
        c+= 1
        
    if s % 2 == 0 and p =='O' or s % 2 != 0 and p =='E':
        print(f'You Lost, I choose {pc}!')
        if c > 0:
                print(f'You won {c} in a row !')
    break