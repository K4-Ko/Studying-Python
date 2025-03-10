# Create a program that reads multiple integer numbers from the user. 
# At the end of the execution, show the average of all the values and the highest and lowest values entered. 
# The program should ask the user if they want to continue entering values.

c = 0
s = 0
q = 0
b = 0
l = 0

while c == 0:
    n = int(input('Type a number: '))
    p = str(input('Would you like to continue [Y] or [N]:' )).upper().strip()[0]
    
    # Counter: divide the sum and we have avg
    q = q + 1
    # Sum
    s = s + n
    
    # highest number and lowest number
    if q ==1:
        b = l = n
    else:
        if n > b:
            b = n 
        if n < l:
            l = n 
        
    if p =='N':
        c = c + 1
        print('You have entered: {} numbers, the average of these numbers is: {} and this is the highest number you have typed: {} and this is the lowest number you have typed: {}'.format(q,s/q,b,l))
