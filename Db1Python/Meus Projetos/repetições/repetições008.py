from psutil import CONN_FIN_WAIT1


num = cont = soma = 0
num = int(input('Digite o número 999 para parar: '))
while num != 999:
    num = int(input('Digite o número 999 para parar: '))
    cont += 1
    soma += num
print ('Você digitou {} e a soma deles é {}'.format (cont, soma))
