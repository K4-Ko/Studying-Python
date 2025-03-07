# Develop a program that reads six integer numbers and displays the sum 
# of only the even ones. If an odd number is entered, ignore it.
s = 0
for c in range (6):
    n = int(input('Type a number: '))
    if n % 2 == 0:
        s += n
print('The sum of the even number is : {}'.format(s))
