'''Refaca o desafio 009, mostrando a tabuada de um numero que o usuario escolher, so
que agora utilizando um laco for.'''

'''numero = int(input('Digite um número: '))
resultado = 0
for c in range(0, 11):
    resultado = numero * c
    print('{} x {} = {}'.format(numero, c, resultado))'''

'''numero = int(input('Digite um número: '))
resultado = 0
for c in range(0, 11):
    resultado = numero * c
    print('{}x{}={}'.format(numero, c, resultado))'''

numero = int(input('Digite um número: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(numero, c, c* numero))