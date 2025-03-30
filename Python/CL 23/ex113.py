# Rewrite the leiaInt() function we created in challenge 104, now including the possibility of handling 
# the input of an invalid number type. 
# Also, create a leiaFloat() function with the same functionality.

def read_int (num):
    
    while True:
        a = input (num).replace(',','.')
        
        try:
            return int(a)
            
        except ValueError:
            print('\033[1;31mTHIS IS NOT AN INTEGER NUMBER, PLEASE TRY AGAIN !\033[m')


def read_float(num):

    while True:
        b = input(num).replace(',','.')

        try:
            return float(b)
            
        except ValueError:
            print('\033[1;31mTHIS IS NOT AN FLOATING-POINT NUMBER, PLEASE TRY AGAIN !\033[m')

            


n = read_int('Type an interger number: ')
m = read_float('Type a floating-point number: ')

print(f' Your integer number is: {n}')
print(f' Your floating number is: {m}')
