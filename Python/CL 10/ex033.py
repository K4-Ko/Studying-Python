# Create a program that reads three numbers and shows which is the largest and which is the smallest.

n1 = int(input('Enter the first number here: '))
n2 = int(input('Enter the second number here: '))
n3 = int(input('Enter the third number here: '))

# Largest
if n1 > n2 and n1 > n3:
  print('The largest number is {}'.format(n1))
if n2 > n1 and n2 > n3:
  print('The largest number is {}'.format(n2))
if n3 > n1 and n3 > n2:
  print('The largest number is {}'.format(n3))

# Smallest
if n1 < n2 and n1 < n3:
  print('The smallest number is {}'.format(n1))
if n2 < n1 and n2 < n3:
  print('The smallest number is {}'.format(n2))
if n3 < n1 and n3 < n2:
  print('The smallest number is {}'.format(n3))
