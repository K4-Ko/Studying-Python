# -*- coding: utf-8 -*-
# O mesmo professor do desafio anterior quer sortear a ordem de apresentacao de trabalhos dos alunos. Faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada 

import random

a1 = input(str('Qual o nome do primeiro aluno: '))
a2 = input(str('Qual o nome do segundo aluno: '))
a3 = input(str('Qual o nome do terceiro aluno: '))
a4 = input(str('Qual o nome do quarto aluno: '))

alunos = (a1,a2,a3,a4)

print('A ordem de apresentacao do trabalho sera:',random.sample(alunos, 4))


