'''Faça um programa que pergunte o preço de três produtos
e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.'''
produto1 = float(input('Qual o preço do primeiro produto: R$'))
produto2 = float(input('Qual o preço do segundo produto: R$'))
produto3 = float(input('Qual o preço do terceiro produto: R$'))
barato = produto3
if produto2<produto1 and produto2<produto3:
    barato = produto2
elif produto1<produto3 and produto1<produto2:
    barato = produto1
print("O produto mais barato custa R${}".format(barato))
