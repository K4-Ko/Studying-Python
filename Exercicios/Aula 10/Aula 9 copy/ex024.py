# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
c = input(str('Digite o nome da cidade: ')).strip()
l = c.split()
f = l[0].upper()
print('SANTO'in f)
