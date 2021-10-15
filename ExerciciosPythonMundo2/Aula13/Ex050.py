'''Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles
que forem pares. Se o valor digitado for impar, desconsidere-o.'''

'''soma = 0
for c in range(0, 6):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma = soma + numero
print('A soma dos números pares informados é {}'.format(soma))'''

soma = 0
contador = 0
for c in range(1, 7):
    numero = int(input('Digite o {}ª valor: '.format(c)))
    if numero % 2 == 0:
        soma = soma + numero
        contador = contador + 1
print('Você informou {} números PARES e a soma foi {}'.format(contador, soma))



