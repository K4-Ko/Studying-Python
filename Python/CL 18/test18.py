person = []
people = []

for c in range(1,5):
    person.append(str(input('Type your name: ')))
    person.append(int(input('Type your age: ')))
    people.append(person[:])
    person.clear()
    
print(people)

