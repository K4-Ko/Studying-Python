# Develop a program that reads the name, age, and gender of 4 people.
# At the end, display:
# - The average age of the group.
# - The name of the oldest man.
# - The number of women under 20 years old.

# t1 : Develop a program that reads the name, age, and gender of 4 people.
# t5 : The number of women under 20 years old

from datetime import date
from math import trunc

ageavg = 0
oldestman = 0
nameoldest = ''
wunder20 = 0

# T1 : Develop a program that reads the name, age, and gender of 4 people. (OK!)
for p in range (1, 5):
    print('========== {} Person =========='.format(p))
    name = str(input('What is your name: '))
    age = date.today().year - (int(input ('What year were you born: ')))
    gender = int(input('What is your gender: Type [1] for Female, Type [2] for Male, Type [3] for Other '))

# T2 : The average age of the group. (OK!)
    ageavg = ageavg + age

# t3 : The age of the oldest man and the name of the oldest man (OK!)
    if gender == 2:
        if age > oldestman:
            oldestman = age
            nameoldest = name

# t5 : The number of women under 20 years old (OK !)
    if gender == 1 and age < 20:
        wunder20 += 1

print('The group age average is: {}'.format(trunc(ageavg/4)))
print('The Oldest mand is called {}  and his age is: {}'.format(nameoldest, oldestman))
print('The amount of women under 20 years old is: {}'.format(wunder20))


