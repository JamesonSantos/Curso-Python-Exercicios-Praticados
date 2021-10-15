'''Crie um programa que simule o funcionamento de uma caixa eletrônico. No início, pergunte
ao usuário qual será o valor a se sacado (número inteiro) e o programa vai informar quantas
cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
'''

'''print('='*30)
print('{:^30}'.format('BANCO ATHENAS'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
cedula = 50
totalcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalcedula += 1
    else:
        if totalcedula >0:
            print(f'Total de {totalcedula} cédulas de R${cedula}')
        if cedula ==50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedula = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO ATHENAS!')'''


print('='*30)
print('{:^30}'.format('BANCO ATHENAS'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$ '))
for nota in [50,20,10,1]:
    quantidade = valor // nota
    valor = valor % nota
    if quantidade > 0:
        print(f'Total de {quantidade} cédulas de R${nota}')
