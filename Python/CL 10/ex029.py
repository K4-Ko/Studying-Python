# Write a program that reads the speed of a car. If it exceeds 80Km/h, display a message saying that it was fined.  
# The fine will cost R$7.00 for each Km above the limit.

v = int(input('What is the speed: '))
m = (v - 80) * 7
if v >= 81:
    print('You will be fined, and the fine amount will be: R$ {}'.format(m))
else:
    print('You are good to go, keep driving!')
