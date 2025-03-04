# -*- coding: utf-8 -*-
# Create a program that reads how much money a person has in their wallet 
# and shows how many US dollars they can buy
# Consider: USD 1.00 = BRL 3.27

n = float(input('What amount would you like to convert?: '))

c = n / 3.27

print('With an amount of BRL: {:.2f}, you can buy USD: {:.2f}'.format(n, c))
