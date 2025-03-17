# This is a number guessing game where the computer generates a random number
# and the player needs to guess it. The game tracks the number of attempts.

# Importing required modules
import random
from time import sleep

# Generate random number between 0 and 5
n = random.randint(0,5)
# Initialize user's guess variable
u = 0
# Initialize attempts counter
a = 0

# Print decorative separator line
print('=-='*15)

# Main game loop - continues until correct guess
while u != n:
    # Get user input for their guess
    u = int(input('I am  thinking about a number, try to guess: '))
    print('Thinking...')
    # Add dramatic pause of 1 second
    sleep(1)
    # If guess is wrong, increment attempt counter
    if u != n:
     a = a + 1
     print('Try again ! {} trials'.format(a))

# Print decorative separator line
print('=-='*15)

# Initialize message variables
f = ''
g = ''
# Set message based on number of attempts
if a >= 3:
   f = 'You SOOOO BAD !' # Message for 3 or more attempts
elif a <= 2:
   g = 'YOU ROCK IT'    # Message for 2 or fewer attempts

# Final message showing the correct number and number of attempts
print('Spot on ! The number was {} It took {} trials.{} '.format(n, a, f, g))
