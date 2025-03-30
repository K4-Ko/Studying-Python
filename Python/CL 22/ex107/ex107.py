# Also, create a program that imports this module and uses some of these functions.

import currencybruno

"a = the amount, b = increase"
print(f'The amount entered was {100} calculating the increase will be: {currencybruno.increase(100,10):.2f}')

"a = the amount, b = discount"
print(f'The amount entered was {100} calculating the discount will be: {currencybruno.decrease(100,10):.2f}')


print(f"The amount entered was {100} and it's double is : {currencybruno.double(100):.2f}")


print(f"The amount entered was {100} and it's half is : {currencybruno.half(100):.2f}")