# Create a program that reads a young person's birth year and informs,
# T1
# Based on their age, whether they still need to enlist in the military, if it is the exact time to enlist, or if they have already missed the deadline.
# T2
# Your program should also display how much time is left or how much time has passed beyond the deadline.

from datetime import date

i = int(input('What is your year of birth: '))
current = date.today().year
age = current - i

if age == 18:
    print('It is the exact time for you to enlist because you are {} years old.'.format(age))
elif age < 18:
    print('You have not yet reached the right age, {} years left.'.format(18 - age))
elif age > 18:
    print('You are {} years late, you should have already enlisted.'.format(age - 18))
