# -*- coding: utf-8 -*-
# Write a program that asks for the number of kilometers driven by a rented car 
# and the number of days it was rented. Calculate the total price to pay, 
# considering that the car costs $60 per day and $0.15 per km driven.

dr = float(input('How many days did you keep the car?: '))
km = float(input('How many kilometers did you drive?: '))

dc = 60 * dr
kr = 0.15 * km
t = dc + kr 

print('The total cost for the rental period ($60 per day) is: ${:.2f}, '
      'The total cost for the kilometers driven ($0.15 per km) is: ${:.2f}, '
      'The final total is: ${:.2f}'.format(dc, kr, t))
