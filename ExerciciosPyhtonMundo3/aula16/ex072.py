''' Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo
teclado (entre 0 e 20) e mostrá-lo por extenso. '''

numeros = ('zero','um','dois','três','quatro','cinco','sei','sete','oito','nove',
           'dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete',
           'dezoito','dezenove','vinte',)

n1 = int(input('Digite um número entre 0 e 20: '))
if n1 >= 0 and n1 <= 20:
    print(numeros.index(n1))
print(c.index(8))