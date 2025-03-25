# Create a program with a function called area() that receives the dimensions  
# of a rectangular plot (width and length) and displays the plot's area.


def line():
    print('--'*20)

def mult(a, b):
    s = a * b
    print(f'The area of your space is {s}m^2')

line()
print(f'{' '*10}Area Calculator')
line()

x = int(input('Type the length: '))
y = int(input('Type the width: '))

mult(x,y)