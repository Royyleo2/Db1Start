'''Faça um Programa que calcule a área de um quadrado, em seguida
mostre o dobro desta área para o usuário'''
base = float(input('Qual a base do seu quadrilátero?'))
altura = float(input('Qual a altura do seu quadrilátero?'))
area = base*altura
dobro_area = area*2
print ('A área do seu quadrilátero é {:.2f} e o dobro dela é {:.2f}'.format(area, dobro_area))
