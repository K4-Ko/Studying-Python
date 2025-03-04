# -*- coding: utf-8 -*-
# Create a program that reads any real number from the keyboard and shows its integer portion on the screen
#   ex: Enter a number: 6.127 The number 6.127 has integer part 6.

from math import trunc

n = float(input('Enter a number: '))
print('The integer part of the entered number {}, is: {}'.format(n, trunc(n)))


