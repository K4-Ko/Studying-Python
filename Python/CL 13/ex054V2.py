
# Create a program that reads the birth year of seven people.
# In the end, display how many of them have not yet reached adulthood 
# and how many are already adults.

from datetime import date

adult = 0
young = 0

for p in range (1, 8):
    print('=========== {} Person ==========='.format(p))
    age = date.today().year - (int(input ('What year were you born: ')))
    
    if age >=18:
        adult = adult + 1
    elif age < 18:
        young = young + 1 

t = ''
if adult > 1:
    t = 'are'
else:
    t = 'is'

tt = ''
if young > 1:
    tt = 'are'
else:
    tt = 'is'

print('From 7 people {} {} adults and {} {} not adults'.format(adult, t, young, tt))