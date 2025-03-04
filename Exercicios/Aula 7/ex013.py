# -*- coding: utf-8 -*-
# Faca um algoritimo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento 

s = float(input('Qual o seu salario: '))

a = s*0.15
t = s + a

print('Considerando que seu salario e: {:.2f} um aumento de 15% no seu salario iria trazer seu salario para: {:.2f}'.format(s, t))
