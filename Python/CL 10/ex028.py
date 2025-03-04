# Write a program that makes the computer "think" of an integer between 0 and 5 and asks the user to try to guess which number was chosen by the computer. 
# The program should display on the screen whether the user won or lost.

import random
from time import sleep

n = random.randint(0, 5)

print('-=-' * 20)
print(' ' * 5, 'I am thinking of a number, try to guess it')
print('-=-' * 20)

g = int(input('Enter your number here: '))

print('Loading...')
sleep(2)

if n == g:
    print('Congratulations, you won!')
else:
    print('You lost, I was thinking of the number: {}!'.format(n))
