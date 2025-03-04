# Create a program that reads a person's full name and then displays the first and last name separately.
# Example: Ana Maria de Souza, First: Ana, Last: Souza

name = input(str('Enter your full name: '))
l = name.split()
print('First name:', l[0], '\nLast name:', l[-1])
