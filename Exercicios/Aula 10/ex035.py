# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Digite o tamanho da primeira reta: '))
r2 = float(input('Digite o tamanho da segunda reta: '))
r3 = float(input('Digite o tamanho da terceira reta: '))

a = r1 + r2 > r3
b = r1 + r3 > r2
c = r2 + r3 > r1

if a and b and c:
    print('Com as retas {}, {} and {}, e possivel formar um triangulo!'.format(r1, r2, r3))
else:
    print('Com as retas {}, {} and {}, nao e possivel formar um triangulo!'.format(r1, r2, r3))