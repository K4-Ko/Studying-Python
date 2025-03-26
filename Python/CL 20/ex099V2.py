# Create a program with a function called higher() that receives multiple parameters  
# with integer values. Your program must analyze all the values and determine which one is the largest. 

from random import randint
from time import sleep

def higher (*num):
    count = h = 0
    print('---'*20)
    print(f'\nAnalyzing the numbers received...')
    sleep(0.5)
    for v in num:
        print(f'{v}', end=' ', flush=True)
        sleep(0.5)
    
        if v > h:
            h = v

        count = count + 1
    sleep(0.5)
    print(f'\nThe highest number received is: {h}\nAnd the total amount of numbers received is: {count}')
    print('---'*20)






# Main program

higher(randint(1,9),randint(1,9),randint(1,9),randint(1,9),randint(1,9),randint(1,9))
higher(randint(1,9),randint(1,9),randint(1,9),randint(1,9))
higher(randint(1,9),randint(1,9))
higher(randint(1,9))
higher()