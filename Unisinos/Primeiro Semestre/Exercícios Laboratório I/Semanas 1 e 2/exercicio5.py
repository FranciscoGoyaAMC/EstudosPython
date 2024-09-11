from time import sleep

numeral1 = int(input('Digite o primeiro número: '))
numeral2 = int(input('Digite o segundo número: '))
numeral3 = int(input('Digite o terceiro número: '))
numeral4 = int(input('Digite o quarto número: '))
numeral5 = int(input('Digite o quinto número: '))

print('Calculando...')
sleep(2)

soma_numerais = numeral1 + numeral2 + numeral3 + numeral4 + numeral5
produto_numerais = numeral1 * numeral2 * numeral3 * numeral4 * numeral5

print(f'{soma_numerais} é o resultado da soma de todos seus valores.')
print(f'{produto_numerais} é o resultado da multiplicação de todos seus valores.')
