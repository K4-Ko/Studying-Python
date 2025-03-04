# -*- coding: utf-8 -*-
import math

# versao simplificada
num = int(input('Digite um numero aqui: '))                       # a parte abaixo (ceil) arredonda o resultado do parenteses a frente
print(print('A raiz quadrado do numero: {}, e: {:.2f}'.format(num, math.ceil(math.sqrt(num)))))

# versao extendida 
num = int(input('Digite um numero aqui: '))
r = math.sqrt(num)                                             
print('A raiz quadrado do numero: {}, e: {:.2f}'.format(num, math.ceil(r)))

# ------------------------------------------------------------------------------------------------------------------------------------
from math import sqrt, floor, ceil

# Quando eu importo parte especifica da biblioteca, ultilizar o "math" como referencia, nao e necessario. exemplo abaixo:

num = int(input('Digite um numero aqui: '))   
print(print('A raiz quadrado do numero: {}, e: {:.2f}'.format(num,ceil(sqrt(num)))))
