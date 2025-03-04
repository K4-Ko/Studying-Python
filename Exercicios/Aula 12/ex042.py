# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais

# – ISÓSCELES: dois lados iguais, um diferente

# – ESCALENO: todos os lados diferentes

# Aula anterior
# Bac

r1 = float(input('Digite o tamanho da primeira reta: '))
r2 = float(input('Digite o tamanho da segunda reta: '))
r3 = float(input('Digite o tamanho da terceira reta: '))

a = r1 + r2 > r3
b = r1 + r3 > r2
c = r2 + r3 > r1

if a and b and c:
    print('Com as retas {}, {} and {}, e possivel formar um triangulo!'.format(r1, r2, r3))

    if r1 == r2 and r2 == r3:
        print('Esse triangulo e um EQUILÁTERO')
    elif r1 == r2 and r1 != r3 or r2 == r3 and r2 != r1 or r1 == r3 and r1 != r2:
        print('Esse triangulo e um ISÓSCELES')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('Esse triangulo e um ESCALENO')
else:
    print('Com as retas {}, {} and {}, nao e possivel formar um triangulo!'.format(r1, r2, r3))





    


