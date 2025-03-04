# -*- coding: utf-8 -*-
# Create a program that reads the length of the opposite leg and the adjacent leg of a right triangle, 
# calculates and displays the length of the hypotenuse.

import math

co = float(input('Value of the Opposite Leg: '))
ca = float(input('Value of the Adjacent Leg: '))

#h1 = pow(co, 2)
#h2 = pow(ca, 2)
#h3 = h1 + h2
#ht = sqrt(h3)

# Simplified code
#ht = math.sqrt(math.pow(co, 2) + math.pow(ca, 2))

# Importing the hypot function
ht = math.hypot(co, ca)

print('With the opposite leg measuring: {}, and the adjacent leg measuring: {}, the hypotenuse length is: {:.2f}'.format(co, ca, ht))
