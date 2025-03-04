# -*- coding: utf-8 -*-
#  Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e a raiz quadrada

n = int(input(' Digite um numero aqui: '))

d = n*2
t = n*3
r = n ** (1/2)

print('O dobro do numero digitado e: {}, Ja o seu triplo e: {}, e a raiz quadrada e: {:.3f}'.format(d, t, r))
