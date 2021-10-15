'''Crie um programa que faça o computador jogar JOKENPÔ com você.'''

'''import random
escolha = str(input('Escolha entre: PEDRA, PAPEL OU TESOURA: '))
lista = ['Pedra', 'Papel', 'Tesoura']
pc = random.choice(lista) #Escolhe um "objeto" da lista
if escolha == pc:
    print('Você escolheu {} e eu {}. Ops! EMPATAMOS!'.format(escolha, pc))
elif 'Pedra' in pc and 'Tesoura' in escolha or 'Tesoura' in pc and 'Papel' in escolha or 'Papel' in pc and 'Pedra' in escolha:
    print('Você escolheu {} e eu {}. Você PERDEU!'.format(escolha, pc))
elif 'Pedra' in escolha and 'Tesoura' in pc or 'Tesoura' in escolha and 'Papel' in pc or 'Papel' in escolha and 'Pedra' in pc:
    print('Você escolheu {} e eu {}. Você VENCEU!'.format(escolha, pc))'''

from random import randint
from time import sleep
lista = ('Pedra', 'Papel', 'Tesoura') #itens a serem escolhidos
pc = randint(0, 2) #comando que vai fazer o computador sortear a lista
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('\033[30mJO\033[m')
sleep(1)
print('\033[31mKEN\033[m')
sleep(1)
print('\033[32mPO!!!\033[m')
sleep(1)
print('-=' * 15)
print('O computador escolheu: {}'.format(lista[pc])) #Escolhe lista na posição pc
print('O jogador escolheu: {}'.format(lista[jogador]))
print('-=' * 15)
if pc == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 1: #computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 2: #computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador ==2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')

