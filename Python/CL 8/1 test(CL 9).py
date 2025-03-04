# -*- coding: utf-8 -*-
import math

# Simplified version
num = int(input('Enter a number here: '))  # The part below (ceil) rounds up the result of the parentheses ahead
print('The square root of the number: {}, is: {:.2f}'.format(num, math.ceil(math.sqrt(num))))

# Extended version
num = int(input('Enter a number here: '))
r = math.sqrt(num)                                             
print('The square root of the number: {}, is: {:.2f}'.format(num, math.ceil(r)))

# ------------------------------------------------------------------------------------------------------------------------------------
from math import sqrt, floor, ceil

# When I import a specific part of the library, using "math" as a reference is not necessary. Example below:

num = int(input('Enter a number here: '))   
print('The square root of the number: {}, is: {:.2f}'.format(num, ceil(sqrt(num))))
