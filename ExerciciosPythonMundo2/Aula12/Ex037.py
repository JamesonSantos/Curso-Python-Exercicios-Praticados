'''Escreva um programa que leia um numero inteiro qualquer e peca para o usuario escolher qual
sera a base de conversao:
-1 para binario.
-2 para octal.
-3 para hexadecimal.'''
numero = int(input('Digite um número inteiro: '))
print('[1] Converter para BINÁRIO \n[2] Converter para OCTAL \n[3] Comverter para HEXADECIMAL234')
escolha = int(input('Escolha a opção: '))
if escolha == 1:
    print('O número {} convertido em BINÁRIO é {:b}'.format(numero, numero))
elif escolha == 2:
    print('O número {} convertido em OCTAL é {:o}'.format(numero, numero))
elif escolha == 3:
    print('O número {} convertido em HEXADECIMAL é {:x}'.format(numero, numero))
