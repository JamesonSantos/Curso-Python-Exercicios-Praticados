velocidade = int(input('Digite a velocidade do caro: Km '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h\nVocê deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')