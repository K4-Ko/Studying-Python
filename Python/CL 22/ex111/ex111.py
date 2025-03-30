# Create a package called utilityCeV that has two internal modules called moeda and dado. 
# Transfer all the functions used in challenges 107, 108, and 109 to the first package and keep everything working.

from utcev.currency import currency_bruno

n = float(input('Type here: '))
currency_bruno.current_resume(n,80,10)