# lanche = () Tupla
# lanche = [] Lista
# lanche = {} Dicionário

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# Tuplas são IMUTÁVEIS

'''
for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
    
for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
    
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
'''

# print(sorted(lanche)) # Mostra em ordem

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
# print(c.count(5)) # Conta quantas vezes está aparecendo o número 5
print(c.index(8)) #Mostra a posição do número'''

pessoa = ('Jameson', 25, 'M', 85.9)
del(pessoa) #Apaga variável
print(pessoa)