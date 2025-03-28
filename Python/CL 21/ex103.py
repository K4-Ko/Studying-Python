# Create a program with a function called form(), which receives two optional parameters: 
# the name of a player and the number of goals he scored. 
# The program should be able to display the player's record, even if some data was not provided correctly.

def form(a=0,b=0):
     return f'Players name is {a}, He has scored {b} goals'
    
# Main program
n = str(input('What is your name: '))
g = input('How many goals was scored?: ')

if g.isnumeric():
     g = int(g)
else:
     g = 0 

if n.strip() == '':
     n = 'N/A'

print(form(n,g))