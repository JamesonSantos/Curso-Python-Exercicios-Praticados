''' Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M e F.
Caso esteja errado, peça a digitação novamente até ter um valor correto. '''

sexo = str(input('Digite seu sexo [M]/[F]: ')).upper()[0].strip()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [M]/[F]: ')).upper()[0].strip()
print('Sexo {} registrado com sucesso'.format(sexo))



