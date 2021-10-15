inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for c in range(inicio, fim + 1, passo):
    print(c)
print('FIM')

'''soma = 0
for c in range(0, 4):
    numero = int(input('Digite um valor: '))
    soma += numero #O mesmo que soma = soma + numero
print('O somatório de todos os valores foi {}'.format(soma))'''