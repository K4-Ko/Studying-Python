# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
from time import sleep

n = random.randint (0, 5)

print('-=-'*20)
print(' '*5, 'Estou pensando em um numero tente advinhar')
print('-=-'*20)

g = int(input('Digite o seu numero aqui: '))

print('Loading...')
sleep(2)


if n == g:
    print ('Parabens, voce ganhou!')
else:
    print('Voce mamou, Eu pensei no numero:{}!'.format(n))
