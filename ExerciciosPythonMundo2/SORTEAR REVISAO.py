from random import randint
from time import sleep
nome = str(input('Qual o seu nome? ')).strip()
print('Tudo bem {}, vou escolher um exercício para você revisar'.format(nome))
exercicio = randint(36, 56)
print('\033[31mEscolhendo...\033[m')
sleep(2)
print('3')
sleep(2)
print('2')
sleep(2)
print('1')
sleep(1)
print('Achei... Você deve revisar o exercício \033[31m{}\033[m.'.format(exercicio))