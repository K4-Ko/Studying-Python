# Create a program with a function called leiaInt(), which works similarly to Python's input() function, 
# but with validation to accept only a numeric value. 
# Example: n = leiaInt('Enter a number: ')

def read_int (num):
    
    while True:
        
        a = input (num)
        if a.isnumeric():
            print('\033[1;32mThis is a valid number !\033[m')
            return a
            
        elif a.isnumeric() == False:
            print('\033[1;31mError !\033[m')
            


n = read_int('Typea number: ')
print(f' You have typed the number: {n}')

   
