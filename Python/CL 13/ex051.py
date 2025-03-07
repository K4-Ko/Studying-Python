# Develop a program that reads the first term and the common difference of an arithmetic progression (AP).
# In the end, display the first 10 terms of this progression.

n = int(input('Type the first number: '))
r = int(input('Type the Progression: '))

for c in range (n, n+10*r , r):
    print('{} ->'.format(c),end=(' '))
print('ACABOU')
    
