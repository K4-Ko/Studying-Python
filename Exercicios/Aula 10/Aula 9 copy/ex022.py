# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

u = input(str('Digite o seu nome inteiro: ')).strip()
r = u.replace(' ','')

s = u.split()
print('O primeiro nome tem:', len(s[0]),'letras,','O nome todo contem:',len(r),'letras', )
print(u.upper(),'and',u.lower())






