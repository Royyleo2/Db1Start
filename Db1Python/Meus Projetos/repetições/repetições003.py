from random import randint
computador = randint(0, 10)
print ('-=-'*10)
print ('Sou seu Computador')
print ('Será que você consegue acertar??')
print ('-=-'*10)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite?'))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print ('Chutou alto demais, tente novamente')
        if jogador < computador:
            print ('Ta baixo, aumenta isso ae')
print ('Parabéns era o número {} e vc Acertou com {} palpites'.format(computador, palpite))

