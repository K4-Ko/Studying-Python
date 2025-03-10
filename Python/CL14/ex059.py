# Create a program that reads two values and displays a menu on the screen:
# 
# [ 1 ] Add
# [ 2 ] Multiply
# [ 3 ] Find the larger number
# [ 4 ] Enter new numbers
# [ 5 ] Exit the program
# 
# The program should perform the requested operation in each case.

from time import sleep

n1 = int(input('Type a number: '))
n2 = int(input('Type another number: '))

while True:
    m = int(input('[ 1 ] Add \n[ 2 ] Multiply\n[ 3 ] Find the larger number\n[ 4 ] Enter new numbers\n[ 5 ] Exit the program\nType here: '))
    
    if m == 1:
        print('{} + {} = {}'.format(n1,n2,n1+n2))
        sleep(2)
    elif m == 2:
        print('{} x {} = {}'.format(n1,n2,n1*n2))
        sleep(2)
    if m == 3:
        if n1 > n2:
            print('{} This is the largest number'.format(n1))
        else:
            print ('{} This is the largest number'.format(n2))
            sleep(2)
    if m == 4:
        n1 = int(input('Type a number: '))
        n2 = int(input('Type another number: '))
    if m == 5:
        break
print ('See you soon!')


