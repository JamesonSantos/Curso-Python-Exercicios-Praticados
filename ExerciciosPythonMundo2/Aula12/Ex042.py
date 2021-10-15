'''Refaça o exercício 035 dos triângulos, acrescentando o recurso de mostrar que tipo de
triângulo será formado.
-Equilátero: Todos os lados iguais.
-Isósceles: Dois lados iguais.
-Escaleno: Todos os lados diferentes.'''
primeiro = float(input('Primeiro segmento: '))
segundo = float(input('Segundo segmento: '))
terceiro = float(input('Terceiro segmento: '))
if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < primeiro + segundo: #Formação de triângulo
    print('Os segmentos PODEM FORMAR um triângulo.')
    #if primeiro == segundo == terceiro:
    if primeiro == segundo and segundo == terceiro: #Triângulo com todos os lados iguais
        print('Triângulo EQUILÁTERO.')
    #elif primeiro != segundo != terceiro != primeiro:
    elif primeiro != segundo and segundo != terceiro and terceiro != primeiro: #Triângulo com todos os lados diferentes
        print('Triângulo ESCALENO.')
    elif primeiro == segundo or segundo == terceiro or terceiro == primeiro: #Triângulo com dois lados iguais
    #else:
        print('Triângulo ISÓSCELES')
else:
    print('Os segmentos NÃO PODEM formar um triângulo.')


