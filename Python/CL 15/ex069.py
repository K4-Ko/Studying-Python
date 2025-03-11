# Create a program that reads the age and gender of several people. For each person registered, the program should ask if the user wants to continue. In the end, show:

# A) how many people are over 18 years old.
# B) how many men were registered.
# C) how many women are under 20 years old.

a = 0
b = 0
c = 0
q = ''
while True:
    print('=-=-=-=-=-=-=-=-=-=-=-= REGISTER =-=-=-=-=-=-=-=-=-=-=-=')
    print('=-='*19)
    #n = str(input('What is your name?: ))
    
    age = int(input('What is your age ?: '))
    gender = int(input ('What is your gender [1] Men [2] Women [3] Other ?: '))
    q = str(input('Would you like to continue ?: [Y] or [N]')).upper().strip()[0]
    # A
    if age > 18:
        a = a + 1
    # B
    if gender == 1:
        b = b + 1
    # C
    if gender == 2 and a < 20:
        c = c + 1

    if q == 'N':
        break

#a
d = ''
if a > 1:
    d = 'are'
else:
    d = 'is'

#b
l = ''
if b > 1:
   l = 'are'
else:
    l = 'is' 

m = ''
if b > 1:
    m = 'men'
else:
    m = 'man'

#c

v = ''
if c > 1:
   v = 'are'
else:
    v = 'is'

w = ''
if c > 1:
    w = 'women'
else:
    w = 'woman' 



print(f'{a} people {d} over 18 years old, {b} {m} {l} registered, {c} {w} {v} under 20 years !')
