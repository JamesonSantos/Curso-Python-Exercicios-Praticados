'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores. Considere 21
para maioridade.'''

contador = 0
from datetime import date
anoatual = date.today().year
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if anoatual - ano >= 21:
        contador = contador + 1
print('Entre as {} pessoas informadas: \n{} São maiores de idade.'.format(c, contador))
print('{} São menores de idade'.format(c - contador))



