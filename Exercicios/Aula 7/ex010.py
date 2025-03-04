# -*- coding: utf-8 -*-
# Crie um programa que leia quanto dinheiro uma pessoa tem na sua carteira e mostre quantos dolares ela pode comprar 
#                           Considere= USD:1,00=R$: 3,27

n = float(input('Qual o valor voce gostaria de coverter?: '))

c = n/3.27

print('Com valor de: R$:{}, voce consegue comprar USD:{:.2f}'.format(n, c))