'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu:
preço normal e condições de pagamento.
-À vista dinheiro/cheque: 10% de desconto.
-À vista no cartão: 5% de desconto.
-Em até 2x no cartão: Preço normal.
-3x ou mais no cartão: 20% de juros'''
print('{:=^40}'.format(' LOJAS CHINESAS '))#{:=^40} Centraliza o nome em 40 caracteres
preco = float(input('Preço do produto R$: '))
print('-' * 40, '\nFORMA DE PAGAMENTO',)
print('-' * 40)
print('[1] À vista em dinheiro \n[2] Cheque \n[3] Cartão de crédito')
escolha1 = int(input('Escolha a forma de pagamento: '))
if escolha1 == 1 or escolha1 == 2:
    print('Você pagará R${:.2f} pelo produto.'.format(preco - (preco * 10) / 100))
elif escolha1 == 3:
    print('-' * 30, '\n[1] À vista \n[2] Parcelado')
    print('-' * 30)
    escolha2 = int(input('Escolha a opção: '))
    if escolha2 == 1:
        print('Você pagará R${:.2f} pelo produto no crédito á vista.'.format(preco - (preco * 5) / 100))
    elif escolha2 == 2:
        escolha3 = int(input('Quantidade de parcelas: '))
        if escolha3 <= 2:
            print('Você pagará R${:.2f} pelo produto em {}x de R${:.2f} SEM JUROS'.format(preco, escolha3, preco / escolha3))
        elif escolha3 >= 3:
            print('Você pagará R${:.2f} pelo produto em {}x de R${:.2f} COM JUROS'.format(preco + (preco * 20) / 100, escolha3, (preco + (preco * 20) / 100) / escolha3))
else:
    print('Opção Inválida')