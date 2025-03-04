# -*- coding: utf-8 -*-
# Create an algorithm that reads a number and displays its double, triple, and square root

n = int(input('Enter a number here: '))

d = n * 2
t = n * 3
r = n ** (1/2)

print('The double of the entered number is: {}, its triple is: {}, and its square root is: {:.3f}'.format(d, t, r))
