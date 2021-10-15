'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e
mostre seu status, de acordo com a tabela abaixo:
-Abaixo de 18.5: Abaixo do peso.
-Entre 18.5 e 25: Peso ideal.
-25 até 30: Sobrepeso.
-30 até 40: Obesidade.
-Acima de 40: Obesidade mórbida.'''
peso = float(input('Digite seu peso: (Kg) '))
altura = float(input('Digite sua altura: (m) '))
imc = peso / (altura  ** 2) #Divide o peso pela altura ao quadrado
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
#elif 30 <= imc <40:
elif imc >= 30 and imc < 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade mórbida')
