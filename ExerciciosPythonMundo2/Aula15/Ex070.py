'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
perguntar se o usuário vai continuar. No final mostre:

a)Qual é o total gasto na compra
b)Quantos produtos custam mais de R$1000
c)Qual é o nome do produto mais barato
'''

print('-' * 30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-' * 30)

total = totalmil = menor = contador = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$ '))
    contador += 1
    total += preco
    if preco > 1000:
        totalmil += 1
    if contador == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totalmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
