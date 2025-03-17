# Create a program that reads the name and weight of multiple people,  
# storing everything in a list. At the end, display:  

# A) How many people were registered.  
# B) A list of the heaviest people.  
# C) A list of the lightest people.  

person = []
people = []

heaviest_people = []
lightest_people = []
c = 0

hpn = ''
hpw = 0

lpn = ''
lpw = 0

while True:
    n = (str(input('Type your name: ')))
    person.append (n)
    w = (float(input('Type your weight: ')))
    
    # Finds the name and weight of the lighesta nd heaviest person
    if c == 0:
        hpw = w
        hpn = n
        lpw = w
        lpn = n
    else:
        if w > hpw:
            hpw = w
            hpn = n
        if w < lpw:
            lpw = w 
            lpn = n 
        
    # add all the names to the list
    person.append (w)
    people.append(person[:])
    person.clear()

    c +=1
    x = (str(input('Would you like to continue adding users ? [Y] to continue [N] to stop. '))).upper().strip()[0]
    if x == 'N':
        break
    if x == 'Y':
        continue


# Compare the weighta and add the heaviers and lighters user to their respective list 
for pessoa in people:
    if pessoa [1] == hpw:
        heaviest_people.append(pessoa[0])

for pessoa in people:
    if pessoa [1] == lpw:
        lightest_people.append(pessoa[0])
        

# A) = How many people were registered. (OK)
print(f'The amount of users registered are:{c}')

# B) A list of the lightest people. 
print(f'The users with the highest weight is/are {heaviest_people} with their weight {hpw} or more')

# C) A list of the lightest people.
print(f'The users with the lightest weight is/are {lightest_people} with their weight {lpw} or less')
