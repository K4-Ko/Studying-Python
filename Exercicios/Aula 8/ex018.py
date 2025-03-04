# -*- coding: utf-8 -*-
# Faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e da tangente desse angulo

import math

a = float(input('Digite o valor do angulo: '))

#sn = math.sin(math.radians(a)) (Tambem e possivel fazer dessa maneira)

ar = math.radians (a)

s = math.sin (ar)
c = math.cos (ar)
t = math.tan (ar)

print('Com o angulo declarado: {} \nO seno: {:.2f} \nO Cosseno: {:.2f} \nE a Tangente: {:.2f}'.format(a, s, c, t))

#print('{:.2f}'.format(sn)) 



