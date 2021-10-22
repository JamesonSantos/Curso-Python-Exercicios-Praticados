''' Crie um programa que tenha uma tupla com várias palavras
(não usar acentos). Depois disso, você deve mostrar, para cada palavra,
quais são as suas vogais. '''

palavras = (('aprender','programar','linguagem','python',
            'curso','gratis','estudar','praticar',
            'trabalhar','mercado','programador','futuro'))


for p in palavras:
    print(f'\nNa palvra {p.upper()} temos: ', end='')
    for letra in p: #Cada palavra já é uma lista de letras
        if letra.lower() in 'aeiou': # Se a lestra estiver no conjunto de vogais
            print(letra, end=' ')

