# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Digite o ano: '))

a = ano % 4 == 0
b = ano % 100 == 0
c = ano % 400 == 0 


if a or b and c:
    print('O ano e bissexto')
else: 
    print('O ano nao e bissexto')
