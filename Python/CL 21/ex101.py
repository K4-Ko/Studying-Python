# Create a program with a function called voto() that receives a person's birth year as a parameter. 
# The function should return a literal value indicating whether the person has a DENIED, OPTIONAL, or MANDATORY vote in elections.
from datetime import date


def vote (age):
    if age < 16:
        return 'Denied'
    elif age >= 16 and age < 18:
       return 'Optional'
    else:
       return 'Mandatory'


while True:
    print('=-='*20)
    b =  int(input('What is your year of birth [Type 999 to stop]: '))
    
    if b == 999:
        break
    
    a = date.today().year - b
    print(f'Your age is {a}, Your vote is: {vote(a)}')
 
    