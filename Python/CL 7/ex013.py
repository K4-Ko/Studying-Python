# -*- coding: utf-8 -*-
# Create an algorithm that reads an employee's salary and displays their new salary with a 15% increase

s = float(input('What is your salary?: '))

a = s * 0.15
t = s + a

print('Considering that your salary is: {:.2f}, a 15% increase would bring your salary to: {:.2f}'.format(s, t))
