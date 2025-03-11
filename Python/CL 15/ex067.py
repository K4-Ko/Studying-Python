 

# Main task
# Create a program that shows the multiplication table of several numbers, one at a time, for each value entered by the user.

# T1 
# The program will be interrupted when the requested number is negative.

n = 0
while n >= 0:
    print('=-='*20)
    n = int(input('\nWhich multiplication table would you like to see? '))
    if n < 0:
        break
    m = 0 
    while m < 10:
        m = m + 1
        print(f'\n{n} x {m} = {n*m}\n')
    
     
        
    

     