# Create a program with a function called type() that receives any text  
# as a parameter and displays a message with an adaptable size.

def type(txt):
    print('-'*len(txt)+4)
    print(f'  {txt}')
    print('-'*len(txt)+4)

t = str(input('What would you like to be printed (Type it here): '))

type(t)