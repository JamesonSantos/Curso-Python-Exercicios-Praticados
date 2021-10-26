'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em
uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão
exibidos todos os valores únicos digitados, em ordem crescente.'''

valores = []
while True:
    r = 0
    nvalor = int(input('Digite um valor: '))
    for c in range(0, len(valores)):
        if valores[c] == nvalor:
            print('Valor Duplicado! Não vou adicionar...')
            r = 1
            break
    if r == 0:
        valores.append(nvalor)
    cont = str(input('Quer continuar? [S/N] '))
    while cont not in 'SsNn':
        cont = str(input('Resposta não válida! Quer continuar? [S/N] '))
    if cont in 'Nn':
        break
valores.sort()
print(f'Você digitou os valores {valores}')