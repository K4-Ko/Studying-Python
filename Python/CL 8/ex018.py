# -*- coding: utf-8 -*-
# Create a program that reads any angle and displays the sine, cosine, and tangent values of that angle.

import math

a = float(input('Enter the angle value: '))

#sn = math.sin(math.radians(a)) (It is also possible to do it this way)

ar = math.radians(a)

s = math.sin(ar)
c = math.cos(ar)
t = math.tan(ar)

print('For the given angle: {} \nSine: {:.2f} \nCosine: {:.2f} \nTangent: {:.2f}'.format(a, s, c, t))

#print('{:.2f}'.format(sn))  
