'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

'''
a = [float(input('Insira um número: ')) for i in range(0, 5)]
print(f'Foram digitados {len(a)} números!')
a.sort(reverse=True)
print(f'Em ordem decrescente {sorted(a, reverse=True)}')
'''

lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar?[S/N] ').upper().strip()[0]
    if resp in 'N':
        break
print('=' * 40, f'\nVocê digitou {len(lista)} números.')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse = True)}')
print('O número 5 aparece na lista!' if 5 in lista else 'o número 5 não aparece na lista!')

