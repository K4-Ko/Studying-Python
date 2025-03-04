# -*- coding: utf-8 -*-
# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Qual a temperatura hoje em Celsius: '))

f = c*1.8+32

print('A conversao da temperatura {:.1f} C, celsius, para fahrenheit seria {:.1f} F'.format(c, f))