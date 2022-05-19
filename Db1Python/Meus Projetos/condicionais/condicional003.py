'''Faça um Programa que verifique se uma letra digitada é "F"
ou "M". Conforme a letra escrever: F - Feminino, M - Masculino,
Sexo Inválido'''
genero = input('Digite F para Feminino e M para Masculino:').upper()
if genero == 'F':
    print('O genero é feminino')
elif genero == 'M':
    print('O genero é masculino')
else:
    print('O genero preenchido com caracter invalido')
