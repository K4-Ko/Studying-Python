# -*- coding: utf-8 -*-
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro, faca um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido 
import random 

a1 = input(str('Digite o nome do primeiro aluno: '))
a2 = input(str('Digite o nome do segundo aluno: '))
a3 = input(str('Digite o nome do terceiro aluno: '))
a4 = input (str('Digite o nome do quarto aluno: '))

s = [a1, a2, a3, a4]

print('O Aluno selecionado para apagar a lousa e:', random.choice(s))


