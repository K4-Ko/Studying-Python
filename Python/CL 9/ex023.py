# Create a program that reads a number from 0 to 9999 and displays each digit separately on the screen.
#   Example: 1834, Thousand: 1, Hundreds: 8, Tens: 3, Units: 4

n = int(input('Enter the number here: '))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Analyzing the number {}'.format(n))
print('Thousand {}'.format(m))
print('Hundreds {}'.format(c))
print('Tens {}'.format(d))
print('Units {}'.format(u))


#           (It gives an error when entering less than 4 digits)        
#print('Thousand:', n[0], 'Hundreds:', n[1], 'Tens:', n[2], 'Units:', n[3])
