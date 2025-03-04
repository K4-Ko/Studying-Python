import random 

a1 = input(str('Qual o nome do primeiro aluno: '))
a2 = input(str('Qual o nome do segundo aluno: '))
a3 = input(str('Qual o nome do terceiro aluno: '))
a4 = input(str('Qual o nome do quarto aluno: '))

l = [a1, a2, a3, a4]
random.shuffle(l)
print('A orde de apresentacao sera:')
print(l)