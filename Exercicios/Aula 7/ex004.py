    # -*- coding: utf-8 -*-
    # Faca um programa que leia algo pelo teclado e mostra  na tela o seu tipo primitivo e todas as informacoes possiveis sobre ele 
    # int=entire number, float=any number.0, boal=true or false and str='string'
d=input('Digite qualquer coisa: ')
print('O tipo do arquivo: ', type(d))
print('O dado digitado e aldabetico? ', d.isalpha())
print('O dado digitado e numerico? ', d.isnumeric())
print('O dado digitado esta totalmente em minusculo? ', d.islower())
print('O dado digitado e um espaco em branco? ', d.isspace())