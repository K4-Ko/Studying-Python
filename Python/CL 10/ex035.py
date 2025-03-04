# Develop a program that reads the length of three line segments and tells the user whether they can form a triangle.

r1 = float(input('Enter the length of the first segment: '))
r2 = float(input('Enter the length of the second segment: '))
r3 = float(input('Enter the length of the third segment: '))

a = r1 + r2 > r3
b = r1 + r3 > r2
c = r2 + r3 > r1

if a and b and c:
    print('With the segments {}, {} and {}, it is possible to form a triangle!'.format(r1, r2, r3))
else:
    print('With the segments {}, {} and {}, it is not possible to form a triangle!'.format(r1, r2, r3))
