# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

# – IMC abaixo de 18,5: Abaixo do Peso

# – Entre 18,5 e 25: Peso Ideal

# – 25 até 30: Sobrepeso

# – 30 até 40: Obesidade

# – Acima de 40: Obesidade Mórbida

from math import pow

p = float(input('Qual o seu peso em kg ?: '))
a = float(input('Qual a sua altura ?: '))

imc = p/(pow (a, 2))
#imc = p/(a**2)


if imc > 40:
    print('Seu IMC e {:.1f}, voce e considerado um Obeso Morbido.'.format(imc))
elif imc < 40 and imc > 30:
    print('Seu IMC {:.1f}, voce e considerado um Obeso'.format(imc))
elif imc < 30 and imc > 25:
    print('Seu IMC {:.1f}, voce esta em sobrepeso'.format(imc))
elif imc < 25 and imc > 18.5:
    print('Seu IMC {:.1f}, voce esta no peso ideal'.format(imc))
else:
    print('Seu IMC {:.1f}, voce esta abaixo do peso'.format(imc))