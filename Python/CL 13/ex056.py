# Develop a program that reads the name, age, and gender of 4 people.
# At the end, display:
# - The average age of the group.
# - The name of the oldest man.
# - The number of women under 20 years old.

n1 = str(input('Type your name: '))
n1a = int(input('Type your age: '))
n1g = int(input('If female type (1), if male type (2) Other (3)'))

n2 = str(input('Type your name: '))
n2a = int(input('Type your age: '))
n2g = int(input('If female type (1), if male type (2) Other (3)'))

n3 = str(input('Type your name: '))
n3a = int(input('Type your age: '))
n3g = int(input('If female type (1), if male type (2) Other (3)'))

n4 = str(input('Type your name: '))
n4a = int(input('Type your age: '))
n4g = int(input('If female type (1), if male type (2) Other (3)'))

# name = [n1, n2 , n3, n4]
# a = [n1a, n2a, n3a, n4a]
# g = [n1g, n2g, n3g, n4g]

# # Age Average 
# average = n1a + n2a + n3a + n4a /4

# oldest = a[0]
# ap = 0

# for x in a:
#     if x > oldest:
#         oldest = x

# for age, x in enumerate (a):
#     if age == oldest:
#         oldest = ap

# # Name of the oldest
# ap = name[ap]

# n20 = 0 

# # Number of woman under 20 
# for c in range (0,5):
#     if c[a] < 20 and c[g] == 1:
#         n20 = n20 + 1

# print (n20)

p1 = [n1, n1a, n1g]
p2 = [n2, n2a, n2g]
p3 = [n3, n3a, n3g]
p4 = [n4, n4a, n4g]

age = p1[2] + p2[2] + p3[2] + p4[2]/4

oldest = p1 [1]

for o in p1[1], p2[1], p3[1] and p4[1]:
    if o > oldest:
        oldest = o

