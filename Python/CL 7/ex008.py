# -*- coding: utf-8 -*-
# Write a program that reads a value in meters and displays it converted to centimeters and millimeters

m = float(input('Enter the number of meters you want to convert: '))

c = m * 100
ml = m * 1000

print('The entered value in meters converted to centimeters is: {:.2f} cm \nThe entered value in meters converted to millimeters is: {:.2f} mm'.format(c, ml))
