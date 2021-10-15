'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma
mensagem no final, de acordo com a média atingida:
-Média abaixo de 5.0: REPROVADO.
-Média entre 5.0 e 6.9: RECUPERAÇÃO.
-Média 7.0 ou superior: APROVADO.'''
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2 #Valor da média do aluno
if media < 5.0:
    print('Você está REPROVADO!')
elif media == 5.0 or media <= 6.9:
    print('Você está de RECUPERAÇÃO!')
elif media >= 7.0:
    print('Você está APROVADO!')