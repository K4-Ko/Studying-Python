# Adapt the code from challenge #107, creating an additional function called moeda() that can display numbers as a formatted monetary value.

import currencybruno

"a = the amount, b = increase"
print(f'The amount entered was € {currencybruno.format_currency(12550)} calculating the increase will be: € {currencybruno.format_currency(currencybruno.increase(12550, 10))}')

"a = the amount, b = discount"
print(f'The amount entered was € {currencybruno.format_currency(145500)} calculating the discount will be: € {currencybruno.format_currency(currencybruno.decrease(145500, 10))}')


print(f"The amount entered was € {currencybruno.format_currency(120000000)} and it's double is : € {currencybruno.format_currency(currencybruno.double(120000000))}")


print(f"The amount entered was € {currencybruno.format_currency(1300000)} and it's half is : € {currencybruno.format_currency(currencybruno.half(1300000))}")