''' Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep
primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))

while True:
    print('-=' * 12)
    print('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos Números\n[5]Sair do programa')
    opcao = int(input('>>>> Qual é a sua opção? '))
    if opcao == 1:
        print('A soma entre {} + {} é {}'.format(primeiro, segundo, primeiro + segundo))
    elif opcao == 2:
        print('O resultado de {} x {} é {}'.format(primeiro, segundo, primeiro * segundo))
    elif opcao == 3:
        print('Entre {} e {} o maior valor é {}'.format(primeiro, segundo, max(primeiro,segundo)))
    elif opcao == 4:
        print('Informe os números novamente:')
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(2)
        print('Fim do programa! Volte sempre!')
        break
    else:
        print('Opção inválida. Tente novamente.')





