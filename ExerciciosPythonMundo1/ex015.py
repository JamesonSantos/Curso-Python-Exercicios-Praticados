dias = int(input('Quantos dias alugados? '))
km = float(input('Qauntos Km rodados? '))
d = (dias * 60) + (km * 0.15)
print('O tatal a pagar é de R${:.2f}'.format(d))
