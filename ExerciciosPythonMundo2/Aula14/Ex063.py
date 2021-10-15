''' Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n
primeiros elementos de uma Sequêencia de Fibonacci.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8'''

print('-'*35, '\nSequência de Fibonacci')
print('-'*35)
numero = int(input('Quantos termos você quer mostrar? '))
termo1 = 0
termo2 = 1
print('~'*35)
print('{} -> {}'.format(termo1, termo2), end='')
contador = 3
while contador <= numero:
    termo3 = termo1 + termo2
    print(' -> {}'.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    contador += 1
print(' -> FIM')
print('~'*35)