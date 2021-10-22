'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares. '''

valores = (int(input('Digite um número: ')),       #Tupla
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))

print(f'O número 9 apareceu {valores.count(9)} vezes')
if 3 in valores: #Se tem 3 na tupla valores
    print(f'O número 3 apareceu pela primeira vez na posição {valores.index(3)+1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in valores: # Se tem números pares
    if n % 2 == 0:
        print(n, end=' ')