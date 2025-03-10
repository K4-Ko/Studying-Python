# Improve the game from CHALLENGE 28, where the computer "thinks" of a number between 0 and 10.  
# Now, the player will keep guessing until they get it right, and at the end,  
# the program should display how many attempts were needed to win.

import random
from time import sleep

n = random.randint(0,5)
u = 0
a = 0

while u != n:
    u = int(input('I am  thinking about a number, try to guess: '))
    print('Thinking...')
    sleep(1)
    if u != n:
     a = a + 1
     print('Try again ! {} trials'.format(a))

f = ''
g = ''
if a >= 3:
   f = 'You SOOOO BAD !'
elif a <= 2:
   g = 'YOU ROCK IT'

print('Spot on ! The number was {} It took {} trials.{} '.format(n, a, f, g))
