print ('-*'*10)
print ('SEQUÊNCIA DE FIBONACCI')
print ('*-'*10)
num = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
cont = 3
print ("~~~"*10)
print ('{} -> {}'.format (t1, t2), end=' ')
while cont <= num:
        t3 = t1 + t2
        print ('-> {}'.format (t3), end= " ")
        t1 = t2
        t2 = t3
        cont += 1
print ('-> FIM')