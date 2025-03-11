# Create a program that simulates the operation of an ATM. At the beginning, ask the user for the amount to be withdrawn (integer number), and the program will inform how many bills of each denomination will be delivered 
# notes
# Consider that the ATM has bills of R$50, R$20, R$10, and R$1.

from math import trunc

# R$50
a = 0
# R$20
b = 0
# R$10
c = 0
# R$1
d = 0

while True:
    m = int(input('How much would you like to cash out ?: '))
    
    a = trunc(m/50)
    m1 = m - a*50
    b = trunc(m1/20)
    m2 = m1 - b*20
    c = trunc(m2/10)
    m3 = m2 - c*10
    d = trunc(m3/1)


   

    print(f'{a} of 50 USD notes, {b} of 20 USD notes, {c} of 10 USD notes, {d} of 1 USD notes')
    
  

