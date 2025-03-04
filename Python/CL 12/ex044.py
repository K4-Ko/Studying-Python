# Create a program that calculates the amount to be paid for a product, 
# considering its normal price and payment condition:

# – Cash payment (money/check): 10% discount
# – Cash payment on card: 5% discount
# – Up to 2x on card: normal price
# – 3x or more on card: 20% interest

p = float(input('What is the price of the product? $: '))

m = int(input('How will you pay for the product? (Enter 1 for cash or check, 2 for card): '))

if m == 2:
    v = int(input('How many installments would you like to divide the total purchase amount into? (Enter 0 for full payment): '))
    if m == 2 and v == 0:
        print('The total amount of your purchase is: ${:.2f} with a one-time card payment.'.format(p - (p * 0.05)))
    elif m == 2 and v <= 2:
        print('The total amount of your purchase is: ${:.2f}, divided into {} installments.'.format(p, v))
    elif m == 2 and v > 2:
        print('The total amount of your purchase is: ${:.2f}, divided into {} installments, each installment will cost: ${:.2f}'.format(p + (p * 0.2), v, ((p + (p * 0.2)) / v)))
elif m == 1:
    print('The total amount of your purchase is: ${:.2f}'.format(p - (p * 0.1)))
