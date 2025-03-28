# Create a program with a function called fatorial() that receives two parameters: 
# the first one indicating the number to be calculated and another called show, 
# which is an optional boolean value indicating whether or not to display the factorial calculation process on the screen.

def fatorial (a=0, b=False):
    x = 1
    for c in range(a, 0, -1):
        x*= c
        if b:
            z = 'x'
            if c == 1:
                z = '='
            print(f'{c} {z}', end = ' ')
    print(x)
    

n1 = int(input('Type any number: '))
fatorial(n1, True)

