'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua
idade:
-Se ele ainda vai se alistar ao serviço militar.
-Se é a hora de se alistar.
-Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date
ano = int(input('Digite o ano de nascimento: '))
anoatual = date.today().year #Ano atual do sistema operacional
idade = anoatual - ano #Subtrai o ano de nascimento do ano atual do sistema
sexo = int(input('[1]Masculino \n[2]Feminino \nOpção:'))
if sexo == 1:
  if idade == 18:
    print('Você tem {} anos. É hora de se alistar ao serviço militar.'.format(idade))
  elif idade <= 16:
    print('Você tem {} anos. Você ainda irá se alistar'.format(idade))
    print('Faltam {} ano(os) para o seu alistamento.'.format(18 - idade))
    saldo = 18 - idade
    tempo = anoatual + saldo
    print('Seu alistamento será em {}'.format(tempo))
  elif idade > 18:
    print('Você tem {} anos. Já passou da hora de se alistar.'.format(idade))
    print('Passou {} ano(os) do seu alistamento.'.format(idade - 18))
    saldo = idade - 18
    tempo = anoatual - saldo
    print('Seu alistamento foi em {}'.format(tempo))
else:
    print('Você não precisa se alistar.')