'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    opt = str(input('Quer continuar? [S/N] ')).strip().upper()
    if opt.startswith('N'):
        break
pares = list(filter(lambda x: x % 2 == 0, lista))
impares = list(filter(lambda x: x % 2 == 1, lista))
print('-=' * 30)
print(f'Foram digitados os números: {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')