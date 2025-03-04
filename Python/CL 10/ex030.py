# Create a program that reads an integer and displays whether it is EVEN or ODD.

n = int(input('Enter your number here: '))

d = n % 2 == 0

#if n % 2 == 0:
if d:
    print('This number is even')
else:
    print('This number is odd')

#if n % 2 == 0:
