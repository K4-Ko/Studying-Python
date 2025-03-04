import random 

s1 = input(str('What is the name of the first student: '))
s2 = input(str('What is the name of the second student: '))
s3 = input(str('What is the name of the third student: '))
s4 = input(str('What is the name of the fourth student: '))

students = [s1, s2, s3, s4]
random.shuffle(students)

print('The presentation order will be:')
print(students)
