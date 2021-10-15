'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
mostra:
 - A média de idade do grupo
 - Qual é o nome do homem mais velho
 - Quantas mulheres tem menos de 20 anos'''

maioridadehomem = 0
homemmaisvelho = ''
contador = 0
media = 0
for pessoa in range(1, 5):
    print('----- {}ª PESSOA -----'.format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    media = media + idade
    if sexo == 'F' and idade < 20:
        contador = contador + 1
    if pessoa == 1 and sexo == 'M':
        maioridadehomem = idade
        homemmaisvelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        homemmaisvelho = nome
print('A média de idade do grupo é de {} anos.'.format(media / 4))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, homemmaisvelho))
print('Ao todo são {} mulheres com menos de {} anos.'.format(contador, 20))

