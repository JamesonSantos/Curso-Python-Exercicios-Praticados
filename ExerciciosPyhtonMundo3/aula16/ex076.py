''' Crie um programa que tenha uma tupla única com nomes de produtos e seus
respectivos preços, na sequência. No final, mostre uma listagem de preços,
organizando os dados em forma tabular. '''

print('-'*41)
print(f'{"LISTAGEM DE PREÇOS":^40}') # Centralizando o nome em 40 espaços
print('-'*41)

listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20,
            'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

for item in listagem:
    if type(item) is str: #Verifica se o tipo é string
        print(f'{item:.<32}', end='') # end='' Faz não quebrar a linha
    else: #Verifica se o tipo é float ou inteiro
        print(f'R$ {item:>6.2f}') # Mostrando com 2 casas decimais
print('-'*41)
