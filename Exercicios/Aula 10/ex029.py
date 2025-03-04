#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('Qual a velocidade: '))
m = (v-80)*7
if v >=81:
    print('Voce vai ser multado, e o Valor do multa sera:R$ {}'.format(m))
else:
    print('Ta on segue em frente!')