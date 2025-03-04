# -*- coding: utf-8 -*-
# Faca um pragrama de leia o comprimento do cateto aposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
import math

co = float(input('Valor do Cateto Oposto: '))
ca = float(input('Valor do Cateto Adjacente: '))

#h1 = pow(co, 2)
#h2 = pow(ca, 2)
#h3 = h1 + h2
#ht = sqrt(h3)

# codigo simplificado
#ht = math.sqrt(math.pow(co, 2)+math. pow(ca ,2))

# importando a funcao hypot
ht = math.hypot(co, ca)

print('Com o valor do cateto oposto em: {}, e o cateto adjacente em: {}, o valor da hipotenusa e: {:.2f}'.format(co, ca, ht))
