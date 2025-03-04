# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#   ex: 1834, Milhar: 1, Centenas: 8, Dezenas: 3, Unidade: 4
n = int(input('Digite o numero aqui: '))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Analisando o numero {}'.format(n))
print('Milhar {}'.format(m))
print('Centenas {}'.format(c))
print('Dezenas {}'.format(d))
print('Unidade {}'.format(u))


#           (Da erro quando digita menos de 4 digitos)        
#print('milhar:',n[0],'Centenas:',n[1],'Dezenas:',n[2],'Unidade:',n[3])