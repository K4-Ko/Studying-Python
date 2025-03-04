# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

# – Média abaixo de 5.0: REPROVADO

# – Média entre 5.0 e 6.9: RECUPERAÇÃO

# – Média 7.0 ou superior: APROVADO

m1 = float(input('Digite sua primeira nota: '))
m2 = float(input('Digite sua segunda nota: '))

m = (m1+m2)/2

if m >=7.0:
    print('Voce foi aprovado, pois sua nota e maior que 7.0. Sua nota foi:{}'.format(m)')
elif m <5.0:
    print('Voce foi reprovado, pois sua media e menor que 5.0. Sua nota foi:{}'.format(m)')
else:
    print('Voce esta de recuperacao! pois a sua media esta entre 5.0 e 6.9, voce tem mais uma chance de melhorar ! Sua nota foi:{}'.format(m))