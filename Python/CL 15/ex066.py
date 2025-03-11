# Create a program that reads integer numbers from the keyboard. The program will stop only when the user enters the value 999, which is the stop condition. In the end, show how many numbers were entered and the sum of them (disregarding the flag).
#================================================================================================================================
# Main Task
#Create a program that reads integer numbers from the keyboard.The program will stop only when the user enters the value 999.

# T1
# Show how many numbers were entered m

#T2
# The sum of them

#=================================================================================================================================
s = q = 0
while True:
    n = int(input('Type any number [Whenever you would like to stop type 999]: '))
    if n == 999:
        break 
    s += n
    q += 1
print (f'You have typed {q}, and the sum of them is: {s}')