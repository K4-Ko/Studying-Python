# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

s = float(input('Qual o seu salario: '))

if s>=1250.00:
    print('Pelo seu salario ser maior que R$1250,00 um aumento de "10%" sera adicionado, Salario antigo R${}, Novo Salario R${}'.format(s, s*0.1+s))
else:
    print('Pelo seu salario ser menor que R$1250,00 um aumento de "15%" sera adicionado, Salario antigo R${}, Novo Salario R${}'.format(s, s*0.15+s))

