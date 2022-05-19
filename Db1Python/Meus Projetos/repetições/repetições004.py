num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número:'))
opção = 0
while opção != 5:
    print ('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opção = int(input('Escolha uma opção:'))
    if opção == 1:
        soma = num1 + num2
        print ('A soma de {} com o {} é {}'.format (num1, num2, soma))
    elif opção == 2:
        mult = num1 * num2
        print ('A multiplicação entre {} e {} é {}'.format (num1, num2, mult))
    elif opção == 3:
        if num1 > num2:
            maior = num1
        elif num1 < num2:
            maior = num2
        else:
            maior = "Nenhum"
        print ('Entra {} e {} o número maior é {}'.format (num1, num2, maior))
    elif opção == 4:
        print ('Informe novamente os números:')
        num1 = int(input('Digite o primeiro número:'))
        num2 = int(input('Digite o segundo número:'))
    elif opção == 5:
        print ('Fim do programa')
    else:
        print ('Opção inválida, tente novamente:')