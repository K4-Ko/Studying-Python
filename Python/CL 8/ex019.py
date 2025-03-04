# -*- coding: utf-8 -*-
# A teacher wants to randomly select one of their four students to erase the board. 
# Create a program to help by reading their names and displaying the chosen student's name.

import random 

a1 = input(str('Enter the name of the first student: '))
a2 = input(str('Enter the name of the second student: '))
a3 = input(str('Enter the name of the third student: '))
a4 = input(str('Enter the name of the fourth student: '))

s = [a1, a2, a3, a4]

print('The student selected to erase the board is:', random.choice(s))
