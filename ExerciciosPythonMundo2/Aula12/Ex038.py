'''Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma
mensagem:
-0 primeiro valor é maior.
-0 segundo valor é maior.
-Não existe valor maior, os dois são iguais.'''
numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))
if numero1 > numero2:
    print('O primeiro valor é MAIOR.')
elif numero2 > numero1:
    print('O segundo valor é MAIOR.')
elif numero1 == numero2:
    print('Não existe valor MAIOR, os dois são IGUAIS.')


