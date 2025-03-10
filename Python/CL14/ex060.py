# Create a program that reads any number and displays its factorial. 
# Example:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input('Type a number: '))

n1 = 1
n2 = n

while n2 != 0:
    n1 = n1 * n2
    n2 = n2 - 1
    if n2 + 1 == n:
        print(n ,end='')
    elif n2 > 1:
        print(' x {}'.format(n2),end='')
    elif n2 == 1:
        print(' x 1 = {}'.format (n1),end='')

