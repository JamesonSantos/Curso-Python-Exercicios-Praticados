'''Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30% do salario ou entao o
emprestimo sera negado.'''
valor = float(input('Valor da casa: R$ '))
salario = float(input('Valor do salário: R$ '))
anos = int(input('Quantidade de anos: '))
prestacao = valor / (anos * 12) #Divide o valor da casa pela quantidade de meses em forma de ano
'''parcela = salario - (salario * 30) / 100 #Subtrai 30% do salário
porcentagem = salario % parcela #Equivale a 30% do salário
#print(p)'''
porcentagem = salario * 30 / 100
if prestacao <= porcentagem:
    print('Seu empréstimo será APROVADO!')
else:
    print('Seu emprèstimo foi NEGADO! ')
