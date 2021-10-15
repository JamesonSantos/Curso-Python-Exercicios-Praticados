'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa decerá perguntar se o usuário quer ou não continuar. No final, mostre:

a) Quantas pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados
c) Quantas mulheres tem menos de 20 anos. '''

maioridade = mulher20 = tothomens = 0

while True:
    print('-' * 30)
    print('{:^30}'.format('CADASTRO DE PESSOAS'))
    print('-' *30)
    idade = int(input('Idade: '))
    if idade >= 18:
        maioridade += 1
    sexo = ''
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    opcao = ''
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'S':






