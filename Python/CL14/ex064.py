# Create a program that reads multiple integer numbers from the user. 
# The program will stop when the user enters the value 999, which is the stop condition.
# In the end, display how many numbers were entered and the sum of them (excluding the stop flag).

c = 0
s = 0
while c >= 0:
    n = int(input('Type a number or type 999 to stop: '))
    c += 1
    s = s + n
    if n == 999:
        print('You have entered {} numbers, the total of the sum is {}'.format(c-1,s-999))
        break
print('END !')

    
    