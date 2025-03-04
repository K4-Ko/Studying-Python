# Crie um programa que faça o computador jogar Jokenpô com você.

import random 
from time import sleep

# LISTA DE JOGADAS:
jogadas = ['', 'PAPEL', 'PEDRA', 'TESOURA']

print('\033[1;31m=-=\033[m'*20)
print(' '*25,'\033[1;32mJokenpô\033[m')
print('\033[1;31m=-=\033[m'*20)

print(' '*5,'\033[1;34mDigite (1) PAPEL     (2) PEDRA     (3) TESOURA\033[m')

p = int(input('\n\033[1;32mDigite aqui sua escolha:\033[m'))
pc = random.randint (1, 3)

print('\033[1;32mPensando...\033[m')
sleep(2)

if p == pc:
    print('Vocês dois colocaram {} isso foi um \033[1;34mEmpate\033[m'.format(jogadas[p]))
elif p == 1 and pc == 2:
    print('Voce \033[1;32mGanhou\033[m pois colocou {}, e eu coloquei {}'.format(jogadas[p], jogadas[pc]))
elif p == 2 and pc == 1:
    print('Voce \033[1;31mPerdeu\033[m pois colocou {}, e eu coloquei {}'.format(jogadas[p], jogadas[pc]))
elif p == 2 and pc == 3:
    print('Voce \033[1;32mGanhou\033[m pois colocou {}, e eu coloquei {}'.format(jogadas[p], jogadas[pc]))
elif p == 3 and pc == 2:
    print('Voce \033[1;31mPerdeu\033[m pois colocou {}, e eu coloquei {}'.format(jogadas[p], jogadas[pc]))
elif p == 1 and pc == 3:
    print('Voce \033[1;32mGanhou\033[m pois colocou {}, e eu coloquei {}'.format(jogadas[p], jogadas[pc]))
elif p == 3 and pc == 1:
    print('Voce \033[1;31mPerdeu\033[m pois colocou {}, e eu coloquei {}'.format(jogadas[p], jogadas[pc]))