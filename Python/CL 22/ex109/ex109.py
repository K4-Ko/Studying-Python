# Modify the functions created in challenge 107 so they accept an additional parameter indicating whether the returned value
# will be formatted by the moeda() function, developed in challenge 108.

import currency_bruno

"a = the amount, b = increase"
print(f'The amount entered was € {currency_bruno.format_currency(12550)} calculating the increase will be: € {currency_bruno.increase(12550, 10,cur = True)}')

"a = the amount, b = discount"
print(f'The amount entered was € {currency_bruno.format_currency(145500)} calculating the discount will be: € {currency_bruno.decrease(145500, 10,cur = True )}')


print(f"The amount entered was € {currency_bruno.format_currency(120000000)} and it's double is : € {currency_bruno.double(120000000,cur = True)}")


print(f"The amount entered was € {currency_bruno.format_currency(1300000)} and it's half is : € {currency_bruno.half(1300000,cur = True)}")