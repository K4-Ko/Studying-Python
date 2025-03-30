# Inside the utilidadesCeV package we created in challenge 111, there is a module called dado. 
# Create a function called leiaDinheiro() that works like the input() function but with data validation 
# to accept only values that are monetary amounts.


from utcev.datas import data
from utcev.currency import currency_bruno

n = data.valid('Type here: ')
currency_bruno.current_resume(n,80,10)