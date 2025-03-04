# Write a Python program that reads any integer and asks the user to choose the conversion base: 
# 1 for binary, 2 for octal, and 3 for hexadecimal.

# T1
# Ask the user to choose the conversion base
# T2
# 1 for binary, 2 for octal, and 3 for hexadecimal.

from time import sleep

n = int(input('Enter an integer: '))

h = hex(n)
b = bin(n)
o = oct(n)

c = int(input('To convert, type the number: 1 for binary, 2 for octal, and 3 for hexadecimal: '))
sleep(2)

if c == 1:
     print('The entered number converted to binary is: {}'.format(b))
elif c == 2:
     print('The entered number converted to octal is: {}'.format(o))
elif c == 3:
     print('The entered number converted to hexadecimal is: {}'.format(h))
else: 
     print('You can only enter 1, 2, or 3')
