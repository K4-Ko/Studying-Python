# -*- coding: utf-8 -*-
# Faca o calculo com dois numero aleatorios, com todas as funcoes possiveis 

n1=int(input('Digite um numero '))
n2=int(input('Digite um numero '))

s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('E a soma {}, é a subtracao {},'.format(s, sub), end =' ')
print('E a multiplicação é {}, a divisão é {:.3f}'.format(m, d), end =' ')
print('E a divisão inteira é {}, e a exponenciação é {}'.format(di, e))
# para formatar a quantidade de casas quando o numero e flutuante {:.(quantas casas depois do ponto)f(de o numero flutuante)}
#                                                                  ex: :.5f (irao aparecer 5 casas depois do ponto)