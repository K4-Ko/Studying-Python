# -*- coding: utf-8 -*-
# Faca um algoritimo que leia o preco de um produto e mostre seu novo preco, com 5% de desconto 

p = float(input('Qual valor total do produto: '))

d = p*0.05
pc = p-d

print('Com o produto no valor total de: {:.2f}, tirando 5% do seu valor, o valor final do produto e: {:.2f}, e o valor subtraido foi {:.2f}' .format(p, pc, d))