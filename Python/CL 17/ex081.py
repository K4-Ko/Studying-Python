# Create a program that will read multiple numbers and store them in a list. 
# After that, display:
# A) How many numbers were entered.
# B) The list of values, sorted in descending order.
# C) Whether the number 5 was entered and if it is in the list or not.

l = []
c = 0 
while True:
    n = int(input('Type a number(to STOP type 999): '))
    if n == 999:
        break
    l.append(n)
    c += 1
    
l.sort(reverse=True)

print(l)

print(f'{c} number was/were entered')

if 5 in l:
    print('The number 5 has been added to the list')
else: 
    print("The number 5 hasn't been added to the list")
