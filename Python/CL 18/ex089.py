# Create a program that reads the name and two grades of multiple students  
# and stores everything in a nested list.  
# At the end, display a report showing each student's average grade  
# and allow the user to view individual grades for each student.  

main_list = []
each_student = []
loop_breaker = ''
c = 0

while True:
    each_student.clear()
    loop_breaker = ''
# Gives the studends their own number
    c += 1
# Collect the students data
    each_student.append(c-1)
    each_student.append(str(input('Type the student full name here: ')))
    each_student.append(int(input('Type the fist grade: ')))
    each_student.append(int(input('Type the second grade: ')))
    main_list.append(each_student[:])
    
# ask if the data inputer wants to keep adding data, if the answer is not Y or N, loop keeps going  
    while loop_breaker not in ['Y','N']:
        loop_breaker = (str(input(' Would you like to continue ? [Y] continue [N] stop: '))).upper().split()[0]
        if loop_breaker not in ['Y','N']:
            print('\033[1;31mTry Again !\033[m', end = '')

    if loop_breaker == 'N':
        break

print('=-='*15)
print(' '*12,'STUDENTS GRADE')
print('=-='*15)
print('N°      NAME                  AVG GRADE')
print('=-='*15)

for x in range(0, c):
    avg = (main_list[x][2] + main_list[x][3]) / 2
    print(f'{main_list[x][0]:<6}{main_list[x][1]:<22}{avg:>8.1f}')

grade_details = 0

while True:
    grade_details = int(input('Type the student number to see the info detailed [999 interrompe]: '))
    if grade_details == 999:
        break
    if grade_details >= 0:
        print(f'{main_list[grade_details]}')