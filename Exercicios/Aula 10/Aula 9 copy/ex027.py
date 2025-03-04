# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#   ex: Ana Maria de Souza, Primeiro: Ana, Ultimo: Souza
nome = input(str('Digite o seu nome inteiro: '))
l = nome.split()
print('O primeiro nome:', l[0],'\nJa o segundo nome:', l[-1])
