# Create a program that reads the weight of five people.
# In the end, display the highest and lowest weight recorded.

p1 = float(input('What is your weight: '))
p2 = float(input('What is your weight: '))
p3 = float(input('What is your weight: '))
p4 = float(input('What is your weight: '))
p5 = float(input('What is your weight: '))

l = [p1, p2, p3 , p4 , p5]

h1 = l[0]
l1 = l[0]

for x in l:
    if x > h1:
        h1 = x
    if x < l1:
        l1 = x

print('The heaviset weight is {}'.format(h1))
print('The lightes wight is {}'.format(l1))

        

