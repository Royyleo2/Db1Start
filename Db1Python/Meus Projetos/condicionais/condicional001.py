'''Faça um Programa que peça dois números e imprima o
maior deles'''
num1 = int(input('Digite um número'))
num2 = int(input('Digite outro número'))
if num1<num2:
    print('O número maior é {}'.format(num2))
elif num1>num2:
    print('O número maior é {}'.format(num1))
else:
    print('Os números são iguais')
