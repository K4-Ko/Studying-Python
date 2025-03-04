# -*- coding: utf-8 -*-

# tempo = int(input('Quanto tempo tem o seu carro: '))
# if tempo <=3:
#     print('Carro novo')
# else:
#     print('Carro usado')
# print('--FIM--')

# #=======================================================================
# #                              SIMPLIFICADO
# tempo = int(input('Quanto tempo tem o seu carro: '))
# print('Carro novo'if tempo <=3 else 'Carro usado')
# print('--FIM--')
# #=======================================================================

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segundo nota: '))
m = (n1 + n2)/2
print('A sua media e: {:.1f}'.format(m))
if m >=5:
    print('Parabens voce passou de ano!')
else:
    print('Voce esta reprovado!')
