'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados
na ordem correta.'''

expr = str(input('Digite a expressão: '))
pi = expr.count('(')
pf = expr.count(')')
if expr.index(')') > expr.index('('):
    if pi == pf:
        print('A expressão é válida.')
    else:
        print('A expressão é inválida.')
else:
    print('Expressão inválida!')