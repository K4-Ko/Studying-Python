# Write a program that reads two integers and compares them, displaying a message on the screen:

# – The first value is greater

# – The second value is greater

# – There is no greater value, both are equal

n1 = int(input('Enter a number: '))
n2 = int(input('Enter another number: '))

if n1 > n2:
    print('The first value is greater, number: {}'.format(n1))
elif n2 > n1:
    print('The second value is greater, number: {}'.format(n2))
else:
    print('The values are equal')
