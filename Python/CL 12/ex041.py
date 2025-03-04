# The National Swimming Confederation needs a program that reads an athlete's year of birth 
# and displays their category according to their age:

# – Up to 9 years old: MIRIM

# – Up to 14 years old: INFANTIL

# – Up to 19 years old: JUNIOR

# – Up to 25 years old: SENIOR

# – Over 25 years old: MASTER

from datetime import date

year_of_birth = int(input('What is your year of birth? '))
current_year = date.today().year
age = current_year - year_of_birth

if age <= 9:
     print('You belong to the Mirim category because you are {} years old'.format(age))
elif age <= 14:
     print('You belong to the Infantil category because you are {} years old'.format(age))
elif age <= 19:
     print('You belong to the Junior category because you are {} years old'.format(age))
elif age <= 25:
     print('You belong to the Senior category because you are {} years old'.format(age))
elif age > 25:
     print('You belong to the Master category because you are {} years old'.format(age))
else:
     print('You entered an invalid date')
