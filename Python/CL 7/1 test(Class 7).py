# -*- coding: utf-8 -*-
# Calculate with two random numbers, using all possible functions

num1 = int(input('Enter a number '))
num2 = int(input('Enter a number '))

sum = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
divide = num1 / num2
int_divide = num1 // num2
exponent = num1 ** num2

print('The sum is {}, the subtraction is {},'.format(sum, subtract), end=' ')
print('The multiplication is {}, the division is {:.3f}'.format(multiply, divide), end=' ')
print('The integer division is {}, and the exponentiation is {}'.format(int_divide, exponent))
# to format the number of decimal places when the number is float {:.(number of places after the decimal point)f(for float number)}
#                                                                  ex: :.5f (5 decimal places will appear)