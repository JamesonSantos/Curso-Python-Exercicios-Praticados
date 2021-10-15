''' Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

'''numero = contador = soma = 0
numero = (int(input('Digite um número [999 para parar]: ')))
while numero != 999:
    contador += 1
    soma += numero
    numero = (int(input('Digite um número [999 para parar]: ')))
print('Você digitou {} números e a soma entre eles foi {}'.format(contador, soma))'''

numero = contador = soma = 0
while numero != 999:
    numero = (int(input('Digite um número [999 para parar]: ')))
    if numero != 999:
        contador += 1
        soma += numero
print('Você digitou {} números e a soma entre eles foi {}'.format(contador, soma))



