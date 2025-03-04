# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite o seu numero aqui: '))

d = n % 2 == 0

#if n % 2  == 0:
if d:
    print('Esse numero e par')
else:
    print('Esse numero e impar')

#if n % 2  == 0: