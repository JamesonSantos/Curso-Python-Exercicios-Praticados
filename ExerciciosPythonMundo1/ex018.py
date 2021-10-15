import math
an = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, math.sin(math.radians(an))))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, math.cos(math.radians(an))))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an, math.tan(math.radians(an))))