s = float(input('Digite seu salário: R$ '))
ns = s + (s * 15 / 100)
print('Seu salário é R${:.2f} e seu novo salário com 15% de aumento é R${:.2f}'.format(s, ns))