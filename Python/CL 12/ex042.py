# Redo CHALLENGE 35 on triangles, adding the feature to show what type of triangle will be formed:

# – EQUILATERAL: all sides equal

# – ISOSCELES: two sides equal, one different

# – SCALENE: all sides different

# Previous lesson
# Bac

r1 = float(input('Enter the length of the first segment: '))
r2 = float(input('Enter the length of the second segment: '))
r3 = float(input('Enter the length of the third segment: '))

a = r1 + r2 > r3
b = r1 + r3 > r2
c = r2 + r3 > r1

if a and b and c:
    print('With the segments {}, {} and {}, it is possible to form a triangle!'.format(r1, r2, r3))

    if r1 == r2 and r2 == r3:
        print('This triangle is EQUILATERAL')
    elif r1 == r2 and r1 != r3 or r2 == r3 and r2 != r1 or r1 == r3 and r1 != r2:
        print('This triangle is ISOSCELES')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('This triangle is SCALENE')
else:
    print('With the segments {}, {} and {}, it is not possible to form a triangle!'.format(r1, r2, r3))
