# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# – Até 9 anos: MIRIM

# – Até 14 anos: INFANTIL

# – Até 19 anos: JÚNIOR

# – Até 25 anos: SÊNIOR

# – Acima de 25 anos: MASTER

from datetime import date

i = int(input('Qual o seu ano de nascimento: '))
atual = date.today().year
d = atual - i

if d <=9:
     print('Voce e da categoria Mirim, pois tem {} anos'.format(d))
elif d <=14:
     print('Voce e da categoria Infantil, pois tem {} anos'.format(d))
elif d <=19:
     print('Voce e da categoria Junior, pois tem {} anos'.format(d))
elif d <=25:
     print('Voce e da categoria Senior, pois tem {} anos'.format(d))
elif d >25:
     print('Voce e da Master, pois tem {}'.format(d))
else:
     print('Voce digitou uma data invalida')
