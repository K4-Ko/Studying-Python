# Write a program that reads any integer N and displays the first N elements of a Fibonacci sequence. 
# Example:
# 0 – 1 – 1 – 2 – 3 – 5 – 8
count = 0
a = 0
b = 1
c = 0

n1 = int(input('How many terms would you like to see: '))

while count < n1:
    print('{} => '.format(c), end='')
    count += 1
    a = b
    b = c
    c = a + b
print('END !')