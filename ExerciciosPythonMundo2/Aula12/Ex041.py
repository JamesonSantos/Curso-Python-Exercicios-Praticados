'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:
-Até 9 anos: MIRIM.
-Até 14 anos:INFANTIL.
-Até 19 anos: JUNIOR.
-Até 25 anos: SÊNIOR.
-Acima: MASTER.'''
from datetime import date
ano = int(input('Digite o ano de nascimento: '))
anoatual = date.today().year #Data atual do sistema operacional
categoria = anoatual - ano #Subtrai ano de nascimento do ano atual do sistema
print('O atleta tem {} anos'.format(categoria))
if categoria <= 9:
    print('Categoria MIRIM')
elif categoria <= 14:
    print('Categoria INFANTIL')
elif categoria <= 19:
    print('Categoria JUNIOR')
elif categoria <= 25:
    print('Categoria SÊNIOR')
elif categoria > 20:
    print('Categoria MASTER')

