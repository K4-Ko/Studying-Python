# -*- coding: utf-8 -*-
# Write a program that converts a temperature entered in degrees Celsius to degrees Fahrenheit.

c = float(input('What is the temperature today in Celsius?: '))

f = c * 1.8 + 32

print('The conversion of {:.1f}°C (Celsius) to Fahrenheit is {:.1f}°F'.format(c, f))
