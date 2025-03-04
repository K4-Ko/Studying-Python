#Faça um programa que leia o ano de nascimento de um jovem e informe, 
# T1
# De acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# T2
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

i = int(input('Qual o seu ano de nascimento: '))
atual = date.today().year
d = atual - i

if d==18:
    print('Esta na hora exata de voce se alistar pois voce esta com {} anos'.format(d))
elif d<18:
    print('Voce ainda nao atingiu a idade certa, faltam {} anos'.format(18-d))
elif d>18:
    print('Voce esta atrasado a {} anos, voce ja deveria ter se alistado'.format(d-18))
