# ... existing code ...

import random 
from time import sleep
import os 

jogadas = ['', 'PAPEL', 'PEDRA', 'TESOURA']

while True:
    print('\033[1;31m=-=\033[m'*20)
    print(' '*25,'\033[1;32mJokenpô\033[m')
    print('\033[1;31m=-=\033[m'*20)

    print(' '*5,'\033[1;34mDigite (1) PAPEL     (2) PEDRA     (3) TESOURA\033[m')

    p = int(input('\n\033[1;32mDigite aqui sua escolha (0 para sair):\033[m'))
    
    if p == 0:
        print('\033[1;31mJogo finalizado. Até a próxima!\033[m')
        break
        
    if p < 0 or p > 3:
        print('\033[1;31mJogada inválida! Tente novamente.\033[m')
        continue
        
    pc = random.randint(1, 3)

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
        print('Voce \033[1;31mPerdeu\033[m pois colocou {}, e eu coloquei {}'.format(jogadas[p], jogadas[pc]))
    elif p == 3 and pc == 1:
        print('Voce \033[1;32mGanhou\033[m pois colocou {}, e eu coloquei {}'.format(jogadas[p], jogadas[pc]))
    
    print('\nPressione Enter para jogar novamente...')
    input()
    
    os.system('cls' if os.name == 'nt' else 'clear')