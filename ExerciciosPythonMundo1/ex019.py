import random
#Escolhe um aleatorio
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
es = random.choice(lista)
print('Entre os alunos: {}, {}, {} e {}. O escolhido para apagar o quadro é: {} '.format(a1, a2, a3, a4, es))

