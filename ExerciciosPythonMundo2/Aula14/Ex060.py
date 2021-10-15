''' Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5x4x3x2x1 = 120'''

'''from math import factorial
numero = int(input('Digite o número a ser fatorado: '))
print('Calculando {}! = {}'.format(numero, factorial(numero)))'''

numero = int(input('Digite o número a ser fatorado: '))
contador = numero
fatorial = 1
print('Calculando {}! ='.format(numero), end=' ')
while contador > 0:
    print('{}'.format(contador), end=' ')
    print('x' if contador > 1 else '=', end=' ')
    fatorial *= contador
    contador -= 1
print('{}'.format(fatorial))

