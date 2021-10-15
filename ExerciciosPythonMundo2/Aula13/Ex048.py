'''Faca um programa que calcule a soma entre todos os numeros impares que sao multiplos
de 3 e que se encontram no intervalo de 1 ate 500.'''

soma = 0
contador = 0
for cont in range(1, 501, 2):
    if cont % 3 ==0:
        contador = contador + 1 # contador += 1
        soma = soma + cont # soma += cont
print('A soma de todos {} os valores solicitados é {}'.format(contador, soma))