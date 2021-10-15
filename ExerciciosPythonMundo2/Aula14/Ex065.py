''' Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''


soma = contador = media = maior = menor = 0
resposta = 'S'
while resposta in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    contador += 1
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma / contador
print('Você digitou {} números e a média foi {}'.format(contador, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))







