# Create a program with a function called type() that receives any text  
# as a parameter and displays a message with an adaptable size.

def type(txt):
    print('-'*len(txt))
    print(txt)
    print('-'*len(txt))

t = str(input('What would you like to be printed (Type it here): '))

type(t)