# Create a program with a function called higher() that receives multiple parameters  
# with integer values. Your program must analyze all the values and determine which one is the largest.  
from random import randint
from time import sleep

def higher (*num): 
    h = 0
    c = 0
    
    l = []
    for v in num:
        l.append(v)
        
        if h == 0:
            h = v
        
        if v > h:
           h = v
        c = c + 1
    print(f'Analazing the numbers entered by the system...')
    sleep(0.5)
    print(f'The numbers entered were {l}')
    sleep(0.5)
    print(f'The amount of numbers entere were: {c}')
    sleep(0.5)
    print(f'The highest number was: {h}')
    print('=-='*10)
        

higher(randint(1,9),randint(1,9),randint(1,9),randint(1,9),randint(1,9),randint(1,9))
higher(randint(1,9),randint(1,9),randint(1,9),randint(1,9))
higher(randint(1,9),randint(1,9))
higher(randint(1,9))
higher()