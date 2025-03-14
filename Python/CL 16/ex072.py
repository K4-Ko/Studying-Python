# Create a program that has a fully populated tuple with a written-out count from zero to twenty.  
# Your program should read a number from the keyboard (between 0 and 20) and display it in full text.

t1 = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten','eleven')
t2 = ('twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
t = t1 + t2

while True:
    n = int(input('Type from number 0 to 20: '))
    if n == 0 or n <= 20:
        break
    else: 
        print('The number is invalid, try again !')
print(f'The number you have typed is {t[n]}')