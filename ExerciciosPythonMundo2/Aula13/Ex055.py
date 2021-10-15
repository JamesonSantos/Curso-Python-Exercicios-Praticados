'''Faca um programa que leia o peso de 5 pessoas. No final, mostre qual foi
o maior e o menor peso lidos.'''

lista = []
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    lista.append(peso) #Adiciona os valores de peso na lista
print('O maior peso digitado foi {}Kg'.format(max(lista)))
print('O menor peso digitado foi {}Kg'.format(min(lista)))

'''
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa'.format(p)))
    if c == 1: #Ler o peso da primeira pessoa
        maior = peso #Maior pesso passa a ser peso
        menor = peso #Menor peso passa a ser peso
    else:
        if peso > maior:
            maior = peso 
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
'''




