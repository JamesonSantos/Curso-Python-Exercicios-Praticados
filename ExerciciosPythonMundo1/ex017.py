'''
n1 = float(input('Comprimento do cateto oposto: '))
n2 = float(input('Comprimento do cateto adjacente: '))
hi = (n1 ** 2 + n2 ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
'''

'''
from math import hypot
n1 = float(input('Comprimento do cateto oposto: '))
n2 = float(input('Comprimento do cateto adjacente: '))
hi = hypot(n1, n2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
'''

'''
import math
n1 = float(input('Comprimento do cateto oposto: '))
n2 = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(n1, n2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
'''

'''import math
n1 = float(input('Comprimento do cateto oposto: '))
n2 = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}'.format(math.hypot(n1, n2)))'''

from math import hypot
n1 = float(input('Comprimento do cateto oposto: '))
n2 = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}'.format(hypot(n1,n2)))