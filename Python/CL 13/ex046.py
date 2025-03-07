

# Create a program that displays a countdown for a fireworks explosion,
# counting from 10 down to 0, with a 1-second pause between each number.

from time import sleep

for c in range(10,0,-1):
    print(c)
    sleep(1)
print ('BOOOM 💥💥💥💥')