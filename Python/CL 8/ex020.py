# -*- coding: utf-8 -*-
# The same teacher from the previous challenge wants to randomly determine the presentation order of student projects.
# Create a program that reads the names of four students and displays the randomized order.

import random

s1 = input(str('What is the name of the first student: '))
s2 = input(str('What is the name of the second student: '))
s3 = input(str('What is the name of the third student: '))
s4 = input(str('What is the name of the fourth student: '))

students = (s1, s2, s3, s4)

print('The presentation order will be:', random.sample(students, 4))
