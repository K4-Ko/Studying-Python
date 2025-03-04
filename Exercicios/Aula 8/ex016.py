# -*- coding: utf-8 -*-
# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porcao inteira 
#   ex: Deigite um numero: 6.127 O numero 6.127 tem a parte inteira 6. 

from math import trunc

n = float(input('Digite um numero: '))
print('A parte inteira do numero digitado {}, e: {}'.format( n, trunc(n)))


