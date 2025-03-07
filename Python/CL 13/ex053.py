# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

#APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

f = str(input('Digite uma frase: ')).upper().strip()
r = f.replace(' ','')
n = len(r)

f1 =''

for c in range (n-1, -1, -1):
    f1 = f1 + r[c]

if r == f1:
    print('A frase digitada sem os espacos foi: {} e ela invertida ficou: {}. Dito isso essa frase e um palíndromo'.format(r, f1))
else:
    print('Essa frase nao e um palíndromo. A frase digita sem os espacos foi: {}, A frase invertida ficou: {}'.format(r, f1))

