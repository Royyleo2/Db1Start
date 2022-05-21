print ('GERADOR DE PA')
print ('-=-' * 10)
primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão da PA:'))
termo = primeiro
cont = 1
while cont <= 20:
        print ('{} ->'.format (termo), end=' ')
        termo = termo + razão
        cont = cont + 1
print ('FIM')