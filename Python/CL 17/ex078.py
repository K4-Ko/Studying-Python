# Create a program that reads 5 numeric values and stores them in a list. 
# At the end, display the largest and smallest values entered and their respective positions in the list.
l = []

for c in range (0, 5):
    n1 = int(input('Type your input: '))
    l.append(n1)

largest = max (l)
smallest = min (l)

print(f'The largest number is {largest}, and its position in the list is: {l.index(largest)}')
print(f'The smallest number is {smallest}, and its position in the list is: {l.index(smallest)}')