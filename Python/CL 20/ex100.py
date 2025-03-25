# Create a program with a list called números and two functions: sorteia() and somaPar().  

from random import randint

# The first function will randomly select 5 numbers and store them in the list.  
def sort():
    l = []
    for c in range (0,5):
        l.append(randint(1,10))
    print(l)
    return l

m = sort()

# The second function will display the sum of all even numbers selected by the previous function.

def sm (m):
    s = 0
    for c in m:
        if c % 2 == 0:
            s+=c
    print(s)
sm(m)