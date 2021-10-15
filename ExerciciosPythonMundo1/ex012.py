p = float(input('Qual é o preço do produto? R$ '))
np = p - (p * 5 / 100)
print('O preço do produto é R${:.2f} e seu preço com 5% de desconto é R${:.2f}'.format(p, np))
