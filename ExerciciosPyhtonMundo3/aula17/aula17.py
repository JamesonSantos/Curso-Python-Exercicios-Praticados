'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7) #Adicionando valor 7 ao elemento
num.sort() #Coloca valores em ordem
#num.sort(reverse=True) #Coloca em ordem do avesso
num.insert(2, 2) #Insere valor 2 na posição 2 refazendo os índices
num.pop() #Elimina o ultimo valor
#num.pop(2) #Elima o valor da posição 2

if 4 in num:
    num.remove(4) #Elimina o primeiro valor 4
else:
    print('Não encontrei o número 4')
print(num)

print(*num, sep=', ')
'*' mostra a lista sem os colchetes/parêntese/chaves e sep é a string entre as variáveis da lista

print(f'Essa lista tem {len(num)} elementos.')'''
