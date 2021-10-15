'''Faca um programa que leia um numero inteiro e diga se ele e ou nao um numero primo.'''

soma = 0
total = 0
numero = int(input('Digite um número: '))
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end=' ')
        total = total + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(numero, total))
if total == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')
