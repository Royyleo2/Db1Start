'''Faça um Programa que verifique se uma letra digitada é
vogal ou consoante.'''
letra = input('Digite uma letra e lhe direi se é Vogal ou Consoante').upper()
vogal = 'AEIOU'
if letra in vogal and letra.isalpha():
    print('A letra {} é uma vogal'.format(letra))
elif letra not in vogal and letra.isalpha():
    print('A letra {} é uma consoante'.format(letra))
else:
    print('Você não digitou uma letra')
