# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

v = int(input('Qual a distancia ate o ponto final da sua viagem: '))
if v <=200:
    print('Pela sua viagem ter a distancia de {}km, o valor da passagem sera R$ {}'.format(v, v*0.5))
else:
    print('Pela sua viagem ter a distancia de {}km, o valor da passagem sera R$ {}'.format(v, v*0.45))
