'''Crie um programa que mostre na tela todos os numeros pares que estao no intervalo entre 1 e 50.'''

print('Números PARES até 50')
for n in range (1, 51):
    if n % 2 == 0:
        print(n, end=' ') #end=' ' mostra na mesma linha

'''for n in range(2, 51, 2):
    print(n, and=' ')
print('Acabou')'''