# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 

from time import sleep

# T1:
# Pergunte o valor da casa, 

c = float(input('Qual o valor da casa ?: '))

# T2
# o salário do comprador  

s = float(input('Qual o seu salario ?: '))

# T3
# Quantos anos ele vai pagar. 

t = int(input('Quantos anos voce pretende pagar a casa ?: '))

# T4
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

p = c / (t*12)
p2 = s*0.3

if p<=p2: 
    print('Parabens, o seu emprestimo de R$:{:.2f}, foi aprovado. A parcela mensal da casa ficara em R$:{:.2f}'.format(c, p))

else:
    print('Infelizmente o seu emprestimo de R$: {:.2f}, nao foi aprovado pois a parcela mensal e maior que "30%" do seu salario'.format(c))
    sleep(2)
    o = str(input('Porem temos uma oferta para voce, voce deseja saber mais sobre (digite Sim ou Nao)?: ')).upper()
    y = 'SIM' in o
    x = s*0.3
    if y:
        print('Porem considerando o salario digitado a cima e o tempo escolhido para pagar a casa, nos conseguimos um emprestimo de R$: {:.2f}'.format(x*420))
    else:
        print('Ok, nos vemos em Breve!')







 



