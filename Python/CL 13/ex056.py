# Develop a program that reads the name, age, and gender of 4 people.
# At the end, display:
#T1 - The average age of the group.
#T2 - The name of the oldest man.
#T3 - The number of women under 20 years old.

from math import trunc

ageavg = 0
oldname = 0
nameold = ''
wunder20 = 0

for p in range (1,5):
    print('=-=-=-=-= {}ªPERSON =-=-=-=-='.format(p))
    name = str(input('Type your name: '))
    age = int(input('Type your age: '))
    gender = int(input('Typer your gender: [1]Female, [2] Male and [3]Other: '))

# Age average 
    ageavg = (ageavg + age)/4

# oldest name and name oldest
    if gender == 2 and age > oldname:
        oldname = age 
        nameold = name

# woman under 20 
    if gender == 1 and age < 20:
        wunder20 = wunder20 + 1

print('The age average is: {}'.format(trunc(ageavg)))
print('The name of the oldest man is: {} and he is {} years old'.format(nameold, oldname))
print('The amount of women under 20 years old is: {}'.format(wunder20))