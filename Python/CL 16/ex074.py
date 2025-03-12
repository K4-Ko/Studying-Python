# Create a program that will generate five random numbers and store them in a tuple.  
# Then, display the list of generated numbers and indicate the smallest and largest values in the tuple.

from random import randint

a = randint(1,5)
b = randint(1,5)
c = randint(1,5)
d = randint(1,5)

t = (a, b, c, d)

print(f'The generated numbers are: {t}')

s = 0 
for c in t:
    if a <= b and a <= c and a <= d:
        s = a
    elif b <= c and b <= d:
        s = b
    elif c <= d:
        s = c
    else:
        s = d

l = 0
for c in t:
    if a >= b and a >= c and a >= d:
        l = a
    elif b >= c and b >= d:
        l = b
    elif c >= d:
        l = c
    else:
        l = d

print(f'The largest amount is {l} and the smaledt amount is {s}')