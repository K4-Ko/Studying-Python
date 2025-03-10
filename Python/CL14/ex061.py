# Rewrite CHALLENGE 51, reading the first term and the ratio of an arithmetic progression (PA),
# and displaying the first 10 terms of the progression using a while loop.

n = int(input('Type a number: '))
p = int(input('Type progression: '))

pa = 0
pg = 0
c = n+9*p

while pg < c:
    if pg == 0:
        print('{} => '.format(n),end ='')
    pa = pa + p
    pg = n + pa
    print('{} => '.format(pg), end='')
print('END')
