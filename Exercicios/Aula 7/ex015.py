# -*- coding: utf-8 -*-
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
    # Carro custa R$60 por dia e R$0,15 por Km rodado
dr = float(input ('Quantos dias voce ficou com o carro: '))
km = float(input ('Quantos Km voce rodou: '))

dc = 60*dr
kr = 0.15*km
t = dc + kr 

print('O total a pagar da estadia (R$60 por dia) com o carro e: R$ {:.2f}, O total a pagar pelos km (R$0,15 por Km) rodados e: R$ {:.2f}, A fatura total ficou: R$ {:.2f}'.format(dc, kr, t))