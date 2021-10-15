distancia = int(input('Qual é a distância da sua viagem? '))
mais = distancia * 0.45
menos = distancia * 0.50
if distancia >= 200:
    print('Você está prestes a começar uma viagem de {:.1f}Km\nE o preço da sua passagem será de R${:.2f}'.format(distancia, mais))
else:
    print('Você está prestes a começar uma viagem de {:.1f}Km\nE o preço da sua passagem será de R$ {:.2f}'.format(distancia, menos))

'''preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45''' # if simplificado
