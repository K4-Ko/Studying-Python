# Create a program that reads any given year and shows if it is a leap year.

year = int(input('Enter the year: '))

a = year % 4 == 0
b = year % 100 == 0
c = year % 400 == 0 

if a or b and c:
    print('The year is a leap year')
else: 
    print('The year is not a leap year')
