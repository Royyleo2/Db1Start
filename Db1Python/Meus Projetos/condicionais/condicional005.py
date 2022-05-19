'''Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada pelo aluno e apresentar:"
A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete;

A mensagem “Reprovado”, se a média for menor do que sete;
A mensagem “Aprovado com Distinção”, se a média for igual a dez.”'''
nome_aluno = input('Digite o nome do aluno:').upper().strip()
nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segundan note:'))
media = (nota1+nota2)/2
if media >= 70.0 and media < 100:
    print('O {} foi aprovado, Parabéns'.format(nome_aluno))
elif media < 70.0:
    print('O {} foi reprovado, Se dedique mais'.format(nome_aluno))
else:
    print('O {} foi Aprovado com Distinção'.format(nome_aluno))
