nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
#Mostra em maiuscula
print('Seu nome em maísculas é {}'.format(nome.upper()))
#Mostra em minuscula
print('Seu nome em minúsculas é {}' .format(nome.lower()))
#Conta os caracteres e tira os espaços
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))