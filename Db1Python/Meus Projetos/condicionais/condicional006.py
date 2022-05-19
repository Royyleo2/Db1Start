'''Faça um Programa que leia três números e mostre o maior e o menor deles. '''
num1 = float(input('Digite primeiro numero:'))
num2 = float(input('Digite segundo numero:'))
num3 = float(input('Digite terceiro numero:'))
maior = num1
if num2>num3 and num2>num1:
    maior = num2
elif num3>num2 and num3>num1:
    maior = num3
else:
    print('Os números são iguais')
print('O maior número é {}'.format(maior))
menor = num2
if num3<num2 and num3<num1:
    menor = num3
elif num1<num2 and num1<num3:
    menor = num1
print('O menor número é {}'.format(menor))
