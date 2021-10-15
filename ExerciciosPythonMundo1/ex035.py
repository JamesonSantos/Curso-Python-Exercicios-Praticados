print('-='*13)
print('Analisador de Triângulos')
print('-='*13)
primeiro = float(input('Primeiro segmento:'))
segundo = float(input('Segundo segmento:'))
terceiro = float(input('Terceiro segmento:'))
if primeiro < segundo + terceiro and terceiro < primeiro + segundo:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo!')

