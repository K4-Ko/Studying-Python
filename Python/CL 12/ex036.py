from time import sleep

# T1:
# Ask for the house price

c = float(input('What is the price of the house?: '))

# T2
# The buyer's salary  

s = float(input('What is your salary?: '))

# T3
# How many years they will pay.

t = int(input('How many years do you plan to pay for the house?: '))

# T4
# The monthly installment cannot exceed 30% of the salary, otherwise the loan will be denied.

p = c / (t * 12)
p2 = s * 0.3

if p <= p2: 
    print('Congratulations, your loan of R$:{:.2f} has been approved. The monthly installment of the house will be R$:{:.2f}'.format(c, p))

else:
    print('Unfortunately, your loan of R$: {:.2f} has not been approved because the monthly installment exceeds "30%" of your salary'.format(c))
    sleep(2)
    o = str(input('However, we have an offer for you. Would you like to know more (type Yes or No)?: ')).upper()
    y = 'YES' in o
    x = s * 0.3
    if y:
        print('However, considering the salary entered above and the chosen repayment period, we can offer a loan of R$: {:.2f}'.format(x * 420))
    else:
        print('Okay, see you soon!')
