# Create a program that will read multiple numbers and store them in a list. 
# After that, create two additional lists: 
# one containing only the even numbers and the other containing only the odd numbers entered. 
# In the end, display the contents of all three generated lists.

l = []
evenl = []
oddl = []

while True:
    n = int(input('Type a number (To stop type 999): '))
    if n == 999:
        break
    l.append(n)
    if n % 2 == 0:
        evenl.append(n)
    elif n % 2 != 0:
        oddl.append(n)

l.sort()
evenl.sort()
oddl.sort()

print(f'Full list: {l}\nEven list: {evenl}\nOdd list: {oddl}')