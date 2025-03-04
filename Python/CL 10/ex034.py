# Write a program that asks for an employee's salary and calculates the amount of their raise.
# For salaries above R$1250.00, calculate a 10% increase.
# For salaries equal to or below this amount, the increase is 15%.

s = float(input('What is your salary: '))

if s >= 1250.00:
    print('Since your salary is greater than R$1250.00, a "10%" increase will be added. Old Salary: R${}, New Salary: R${}'.format(s, s*0.1+s))
else:
    print('Since your salary is less than R$1250.00, a "15%" increase will be added. Old Salary: R${}, New Salary: R${}'.format(s, s*0.15+s))
