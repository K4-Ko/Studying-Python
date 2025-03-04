# -*- coding: utf-8 -*-
# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros 

m = float(input('Digite quantos metros voce deseja converter: '))

c = m*100
ml = m*1000 

print('O valor em metros digitado convertido em centimetros seria: {:.2f} cm \nO valor digitado em metros convertido em milimetros seria: {:.2f} mm'.format(c,ml))