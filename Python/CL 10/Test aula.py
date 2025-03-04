# -*- coding: utf-8 -*-

# time = int(input('How old is your car? '))
# if time <= 3:
#     print('New car')
# else:
#     print('Used car')
# print('--END--')

# #=======================================================================
# #                              SIMPLIFIED
# time = int(input('How old is your car? '))
# print('New car' if time <= 3 else 'Used car')
# print('--END--')
# #=======================================================================

n1 = float(input('Enter the first grade: '))
n2 = float(input('Enter the second grade: '))
m = (n1 + n2)/2
print('Your average grade is: {:.1f}'.format(m))
if m >= 5:
    print('Congratulations, you passed!')
else:
    print('You failed!')
