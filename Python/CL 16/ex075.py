# Develop a program that reads four values from the keyboard and stores them in a tuple.  
# In the end, display:

# A) How many times the value 9 appeared.  
# B) The position where the first value 3 was entered.  
# C) Which numbers were even.

n1 = int(input('Type a number: '))
n2 = int(input('Type a number: '))
n3 = int(input('Type a number: '))
n4 = int(input('Type a number: '))

t = (n1, n2 ,n3, n4)

n9 = 0
p3 = 0
e = 0

for c in t:
    n9 = t.count(9)
    
    if n1 == 3 or n2 == 3 or n3 == 3 or n4 == 3:
        p3 = t.index(3)
    
if n1 % 2 == 0: 
        e = e + 1
if n2 % 2 == 0: 
        e = e + 1
if n3 % 2 == 0: 
        e = e + 1
if n4 % 2 == 0: 
        e = e + 1

pt =''
if n1 == 3 or n2 == 3 or n3 == 3 or n4 == 3:
 pt = f', times The number 3 posistion was {p3}'


print(f'The number 9 has appeared {n9}{pt}, {e} numbers were even.')
    