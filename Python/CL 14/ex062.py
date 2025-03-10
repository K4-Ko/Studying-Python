# Improve CHALLENGE 61 by asking the user if they want to show more terms.
# The program will stop when the user indicates they want to show 0 terms.
n1 = int(input('Type the first number: '))
n2 = int(input('Typer the second number: '))

t = n1
count = 1

while count <= 10:
    print('{} => '.format(t),end='')
    t += n2
    count+= 1
    if count == 10:
        a = int(input('\nHow many terms would you like to see?: '))
        if a > 0 :
            count = count - a
        elif a == 0:    
            break
print('END')   