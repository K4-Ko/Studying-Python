# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

#APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

f = str(input('Type a phrase here: ')).upper().strip()
r = f.replace(' ','')
n = len(r)

f1 = 0

for c in range (n-1, 0, 1):
