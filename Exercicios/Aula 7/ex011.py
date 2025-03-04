# -*- coding: utf-8 -*-
# Faca um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessario para pintalo...
# ...sabendo que cada litro de tinta, pinta uma area de 2 metros quadrados

h = float(input('Qual a Altura da Sua Parede: '))
l = float(input('Qual a Largura da Sua Parede: '))

a = h*l
t = a/2

print('Para voce pintar a sua parede das seguintes dimensoes, Altura {} M, e Largura {} M'.format(h, l), end ='')
print(', Area total {} m2, voce ira precisar de {} Litros de tinta'.format(a, t))