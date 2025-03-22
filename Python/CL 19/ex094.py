# Create a program that reads the name, gender, and age of multiple people, 
# storing each person's data in a dictionary and all dictionaries in a list. 
# In the end, display:

from math import trunc

people = []
person = {}

while True:
    person ['name'] = str(input('Type your name ?:  '))
    person ['age'] = int(input('What is your age ?:  '))
    person ['gender'] = str(input('What is your gender ?: ')).upper().strip()
    people.append(person.copy())
    
    while True:
        q = str(input('[Y - to continue] and [N - to stop]: ')).upper().strip()[0]
        if q in 'YN':
            break
        print('Try Again !')
    
    if q == 'N':
        break 
    elif q == 'N':
        continue

# A) The number of registered people
print(f'The amount of people registered is: {len(people)}')

# B) The average age
s = 0

for x in people:
    s += x['age']
print(f'The age average is {trunc(s/len(people))}')

media = s/len(people)

# C) A list of women
m = []
for x in people:
    if x['gender'] == 'F':
        m.append(x['name'])
print(f'The list of women is: {m}')

# D) A list of people older than the average age
over_avg = []

for x in people:
    if x['age']> media:
        over_avg.append(x['name'])
print(f'The list above the average is: {over_avg}')