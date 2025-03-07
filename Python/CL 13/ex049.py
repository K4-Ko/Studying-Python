# Redo CHALLENGE 9, displaying the multiplication table of a number chosen by the user, but this time using a for loop.

n = int(input('Type a numer to discover to multiplication table up to 10: '))
m = 0 
for c in range (1,11,1):
    m = c*n
    print ('{} x {} = {}'.format(n, c, m))