''' Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo
teclado (entre 0 e 20) e mostrá-lo por extenso. '''

extensos = ('zero','um','dois','três','quatro','cinco','sei','sete','oito','nove',
           'dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete',
           'dezoito','dezenove','vinte',)

numero = int(input('Digite um número entre 0 e 20: '))
while numero not in range(0, 21):
    numero = int(input('[ERRO] Digite um número entre 0 e 20: '))
print(f'Você digitou o número {extensos[numero]}')