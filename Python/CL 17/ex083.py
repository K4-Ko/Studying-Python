# Create a program where the user enters any expression that uses parentheses. 
# Your application should analyze whether the given expression has correctly 
# opened and closed parentheses in the correct order.

n = str(input('Type a mathematic expression here: '))
l = []

for sim in n:
    if sim == '(':
        l.append('(')
    
    elif sim == ')':
        if len(l) > 0:
            l.pop()
    else:
        l.append(')')
        break

if len(l) == 0:
    print('Your expression is valid !')
else:
    print('Your expression is not valid !')

