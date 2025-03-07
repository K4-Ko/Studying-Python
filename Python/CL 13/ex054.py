# Create a program that reads the birth year of seven people.
# In the end, display how many of them have not yet reached adulthood 
# and how many are already adults.

from datetime import date

p1 = date.today().year - int(input('What year were you born: '))
p2 = date.today().year - int(input('What year were you born: '))
p3 = date.today().year - int(input('What year were you born: '))
p4 = date.today().year - int(input('What year were you born: '))
p5 = date.today().year - int(input('What year were you born: '))
p6 = date.today().year - int(input('What year were you born: '))
p7 = date.today().year - int(input('What year were you born: '))

l = [p1,p2,p3,p4,p5,p6,p7]
a = 0
o = 0

for c in range (0, 7):
    if l[c] >= 18:
        a += 1
    else:
        o += 1

print('The number of adults is: {} and the number of young people or children is: {}'.format(a, o))