''' Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os
10 primeiros termos da progressão usando a estrutura while.'''

'''print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
decimo = primeiro + (10 * razao)
while primeiro < decimo:
    print(primeiro, '->', end=' ')
    primeiro += razao
print('FIM')'''

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1
while contador <= 10:
    print('{} ->'.format(termo), end=' ')
    termo += razao
    contador += 1
print('FIM')



