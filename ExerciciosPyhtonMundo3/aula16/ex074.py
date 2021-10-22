''' Crie um programa que vai gerar cinco números aleatórios e colocar em uma
tupla. Depois disso, mostre a listagem de números gerados e também indique o
menor e o maior valor que estão na tupla.'''

from random import sample

numeros = tuple(sample(range(10), 5)) #Sorteando 5 numeroa aleatorios dos 10
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

