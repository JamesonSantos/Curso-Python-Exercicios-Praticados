a = [2, 3, 4, 7]
b = a[:] #b recebe todos os itens de a. Criando uma cópia de a no b
b[2] = 8
print(f'A lista A: {a}')
print(f'A lista B: {b}')
