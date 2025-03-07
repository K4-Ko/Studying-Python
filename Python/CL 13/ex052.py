# Create a program that reads an integer number and determines whether it is a prime number or not.

import math

n = int(input('Type a number: '))

if n == 2:
    print('This number is prime')
elif n < 2 or (n % 2 == 0 and n > 2):
    print('This number is not prime')
else:
    n1 = True

    for c in range(3, n, 2):
        if n % c == 0:
            n1 = False
            break

    if n1:
        print('This number is prime')
    else:
        print('This number is not prime')
