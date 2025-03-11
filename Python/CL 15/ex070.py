# Create a program that reads the name and price of several products. The program should ask if the user wants to continue or not. In the end, show:

# A) the total amount spent on the purchase.
# B) how many products cost more than R$1000.
# C) the name of the cheapest product.

a = 0
b = 0
c = 0
d = 0
e = ''
q = ''

while True:
    product = str(input('What is the name of the product?: '))
    price = int(input('What is the price of this product?: '))
    q = str(input('Would you like to continue ?: [Y] or [N]')).upper().strip()[0]
    
    # A
    if price > 1:
        a = a + price
    # B
    if price > 1000:
        b = b + 1
    # C
    if  c == 0:
        c = price 
        e = product
    else:
        if price < c:
            c = price 
            e = product
    if q == 'N':
        break

v = ''
if b <= 1:
 v = 'is'
else:
    v = 'are'


print(f'The total amount spend was: {a}, The amount of products over 1000 USD {v} {b}, The name of the cheapest product is: {e}')
