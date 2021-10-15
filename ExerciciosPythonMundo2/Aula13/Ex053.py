'''Crie um programa que leia uma frase qualquer e diga se ela é um palindromo,
desconsiderando os espaços. Ex:
- APOS A SOPA
- A SACADA DA CASA
- A TORRE DA DERROTA
- O LOBO AMA O BOLO
- ANOTARAM A DATA DA MARATONA'''

nome = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
inverso = nome[::-1]
if nome == inverso:
    print('O inverso de {} é {}'.format(nome, inverso))
    print('A frase digitada é um palíndromo!')
else:
    print('O inverso de {} é {}'.format(nome, inverso))
    print('A frase digitada não é um palíndromo!')
