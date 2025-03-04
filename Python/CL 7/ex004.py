# -*- coding: utf-8 -*-
# Create a program that reads an input from the keyboard and displays its primitive type 
# and all possible information about it
# int = entire number, float = any number.0, bool = true or false, and str = 'string'

d = input('Enter anything: ')
print('The type of the input: ', type(d))
print('Is the entered data alphabetic? ', d.isalpha())
print('Is the entered data numeric? ', d.isnumeric())
print('Is the entered data completely lowercase? ', d.islower())
print('Is the entered data a whitespace? ', d.isspace())
