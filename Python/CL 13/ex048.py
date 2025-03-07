# Create a program that calculates the sum of all numbers that are multiples of three 
# within the range from 1 to 500.

s = 0
for x in range(0, 500, 3):
    s += x
print('The sum of all numbers that are multiples of three is {}'.format(s))
