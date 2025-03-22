# Create a program that reads a person's name, year of birth, and work card number, 
# then stores them (along with age) in a dictionary. 
# If the work card number is different from ZERO, the dictionary should also include 
# the year of hiring and the salary. 
# Calculate and add, besides the age, the age at which the person will retire.
from datetime import date

user_list = {}

while True:
    
    user_list['name'] = str(input('What is your name: '))
    user_list['age'] = date.today().year - int(input('Year of birth: '))
    user_list['pps'] = int(input('What is your PPS number: [Type 0 if does not have]'))
    
    if user_list['pps'] == 0:
        print('Not available at this time !')
    
    else:
        user_list['work date'] = date.today().year - int(input('When were you hired for the first time: '))
        user_list['salary'] = int(input('What is your salary: '))
        break


n = 35 - user_list ['work date'] 

print(f'Your name is: {user_list['name']} \nYour age is: {user_list['age']}')
print(f'Salary: {user_list['salary']}')
print(f'You will retire with {user_list['age']+n}')
