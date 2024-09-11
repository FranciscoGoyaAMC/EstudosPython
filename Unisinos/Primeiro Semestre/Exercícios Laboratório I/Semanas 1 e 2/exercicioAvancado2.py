from time import sleep

print('-=' * 10)
print('Bhaskara')
print('-=' * 10)
sleep(0.5)

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

print('Calculando...')
sleep(2)


x_linha = ((b * -1) + (b**2 - 4 * a * c) ** (1/2)) / (2 * a)
x_duas_linha = ((b * -1) - (b**2 - 4 * a * c) ** (1/2)) / (2 * a)
print(f"O resultado das raízes são: x': {x_linha}, x'': {x_duas_linha}")
