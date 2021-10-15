'''print('-=-'*19, '\nVou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*19)
numero = int(input('Em que número eu pensei? '))
import random
lista = [0, 1, 2, 3, 4, 5]
numero2 = random.choice(lista)
if numero2 == numero:
    print('PARABÉNS! Vcoê acertou!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(numero2, numero))'''

from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "SORTEAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print("PARABENS! Você conseguiu me vencer!")
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))

