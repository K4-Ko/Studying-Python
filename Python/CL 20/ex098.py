# Create a program with a function called contador() that receives three parameters:  
# start, end, and step. Your program must perform three counts using the created function:  

from time import sleep

#def space
def l ():
    print('=-='*10)

def a():
    for c in range(1, 11):
        print(c, end=' ', flush=True)  # flush força a saída imediata
        sleep(0.5)
    print()


def b():
    for x in range (10, -1, -2): 
        print(x, end=' ', flush=True)  
        sleep(0.5)
    print()

def c(i, f, p):
    for z in range (i, f, p): 
        print(z, end=' ', flush=True)
        sleep(0.5)
    print()



# a) From 1 to 10, counting by 1  

a()

l()
# b) From 10 to 0, counting by 2  

b()

l()

# c) A custom count  

i = int(input('What number would you like tthe counter to start?: '))
f = int(input('What number would you like the counter to stop?: '))
p = int(input('What step would you like the counter to take?: ')) 

if i < f:
    f = f + 1 

elif i > f:
    f = f -1

if i > f and p == 0:
    p = -1
elif i < f and p == 0:
    p = 1
l()
c(i, f, p)