# -*- coding: utf-8 -*-
# Create a program that reads the width and height of a wall in meters, calculates its area, 
# and determines the amount of paint needed to paint it...
# ...considering that each liter of paint covers an area of 2 square meters.

h = float(input('What is the height of your wall (in meters)?: '))
l = float(input('What is the width of your wall (in meters)?: '))

a = h * l
t = a / 2

print('To paint your wall with the following dimensions: Height {} m and Width {} m'.format(h, l), end='')
print(', Total area {} m², you will need {} liters of paint'.format(a, t))
