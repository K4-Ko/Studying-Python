# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# # – em até 2x no cartão: preço normal 
# – 3x ou mais no cartão: 20% de juros

p = float(input('Qual o preco do produto? R$: '))

m = int(input('Como voce vai pagar o produto(Digite 1 para dinheiro ou cheque, 2 para cartao): '))

if m == 2:
    v = int(input('Quantas vezes voce gostaria de dividir o valot total da compra (Digite 0 para pagar a vista): '))
    if m == 2 and v == 0:
        print('O valor total da sua compra e: R${:.2f} a vista no cartao'.format(p-(p*0.05)))
    elif m == 2 and v <= 2:
        print('O valor total da sua compra e: R${:.2f} e divido em: {} vezes'.format(p, v))
    elif m == 2 and v > 2:
        print('O valor total da sua compra e: R${:.2f} e dividido em {} vezes, cada parcela custara: R${:.2f}'.format(p+(p*0.2), v,((p+(p*0.2))/v)))
elif m == 1:
    print('O valor total da sua compra e: R${:.2f}'.format(p-(p*0.1)))