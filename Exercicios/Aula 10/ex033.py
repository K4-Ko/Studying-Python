# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite aqui o primeiro numero: '))
n2 = int(input('Digite aqui o segundo numero: '))
n3 = int(input('Digite aqui o terceiro numero: '))

# Maior 
if n1 > n2 and n1 > n3:
  print('O maior numero e o {}'.format(n1))
if n2 > n1 and n1 > n3:
  print('O maior numero e o {}'.format(n2))
if n3 > n1 and n1 > n2:
  print('O maior numero e o {}'.format(n3))

#Menor
if n1 < n2 and n1 < n3:
  print('O menor numero e o {}'.format(n1))
if n2 < n1 and n2 < n3:
  print('O menor numero e o {}'.format(n2))
if n3 < n1 and n3 < n2:
  print('O menor numero e o {}'.format(n3))






   