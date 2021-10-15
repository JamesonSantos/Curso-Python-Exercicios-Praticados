from random import choice
from time import sleep
lista = [1, 2, 4, 5, 6, 7, 10, 12, 13, 14, 15, 17, 19, 20, 21, 22, 23, 25, 26, 31, 34, 36, 40, 42, 50]
int = str(input('Aperte [1] para sortear ')).strip()
print('Vamos começar... Vou escolher um número para você...')
exercicio = choice(lista)
print('\033[31mEscolhendo...\033[m')
sleep(2)
print('3')
sleep(2)
print('2')
sleep(2)
print('1')
sleep(1)
print('Achei... O grande vencedor do conjunto de panelas Royal VKB foi o Nº \033[31m{}\033[m.'.format(exercicio))



