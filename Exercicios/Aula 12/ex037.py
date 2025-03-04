# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
#T1
#peça para o usuário escolher qual será a base de conversão
#T2
# 1 para binário, 2 para octal e 3 para hexadecimal.

from time import sleep

n = int(input('Escreva um numero inteiro: '))

h = hex(n)
b = bin(n)
o = oct(n)

c = int(input('Para transformar digite o numero, 1 para binário, 2 para octal e 3 para hexadecimal:'))
sleep(2)

if c == 1:
     print('O numero digitado convertido para binario e: {}'.format(b))
elif c == 2:
     print('O numero digitado convertido para octal e: {}'.format(o))
elif c == 3:
     print('O numero digitado convertido para octal e: {}'.format(h))
else: 
     print('Voce pode apenas digitar 1, 2 ou 3')


