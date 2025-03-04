# -*- coding: utf-8 -*-
# Create an algorithm that reads the price of a product and displays its new price with a 5% discount

p = float(input('What is the total price of the product?: '))

d = p * 0.05
pc = p - d

print('With the product priced at: {:.2f}, applying a 5% discount, the final price is: {:.2f}, and the amount deducted was {:.2f}'.format(p, pc, d))
