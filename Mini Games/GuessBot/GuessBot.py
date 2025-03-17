# Write a program that makes the computer "think" of an integer between 0 and 5 and asks the user to try to guess which number was chosen by the computer. 
# The program should display on the screen whether the user won or lost.

# Import the random module to generate random numbers
# Import sleep function from time module to add delays
import random
from time import sleep

# Generate a random integer between 0 and 5 (inclusive)
n = random.randint(0, 5)

# Print decorative separator line with '-=-' repeated 20 times
print('-=-' * 20)
# Print the game introduction message, with 5 spaces of padding
print(' ' * 5, 'I am thinking of a number, try to guess it')
# Print another decorative separator line
print('-=-' * 20)

# Get user input and convert it to an integer
g = int(input('Enter your number here: '))

# Display "Loading..." message
print('Loading...')
# Pause the program for 2 seconds to create suspense
sleep(2)

# Check if the user's guess matches the computer's number
if n == g:
    # If the numbers match, display winning message
    print('Congratulations, you won!')
else:
    # If the numbers don't match, display losing message and reveal the correct number
    print('You lost, I was thinking of the number: {}!'.format(n))
