# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
f = input('Digite uma frase: ').upper()
l1 = f.count('A')
l2 = f.find('A')
l3 = f.rfind('A')
print('Na frase digita contem:', l1,'"A"','\nO primeiro A aparece na seguinte posicao:', l2,'\nJa o ultimo A aparece na seguinte posicao:', l3)