
# Create a program that reads a student's name and average grade, 
n = str(input('Student name: '))
avg = float(input('What is the student average grade: '))

# also storing their status in a dictionary.
student_dict = {'Nome': n, 'avg': avg }

# In the end, display the content of the structure on the screen.
if avg >= 5:
    print(f'{student_dict['Nome']} has been approved with an average: {student_dict['avg']}')
else:
    print(f'{student_dict['Nome']} was not approved with an average: {student_dict['avg']}')