# Create a program that reads two grades from a student and calculates their average, 
# displaying a message at the end according to the achieved average:

# – Average below 5.0: FAILED

# – Average between 5.0 and 6.9: RECOVERY

# – Average 7.0 or higher: PASSED

g1 = float(input('Enter your first grade: '))
g2 = float(input('Enter your second grade: '))

average = (g1 + g2) / 2

if average >= 7.0:
    print('You passed because your grade is higher than 7.0. Your grade was: {}'.format(average))
elif average < 5.0:
    print('You failed because your average is lower than 5.0. Your grade was: {}'.format(average))
else:
    print('You are in recovery! Your average is between 5.0 and 6.9, you have another chance to improve! Your grade was: {}'.format(average))
