valor1 = int(input('Digite um número: '))
valor2 = int(input('Digite outro número: '))
if valor1 < 0 or valor2 < 0:
    print('Erro! Valor negativo')
elif valor1 > valor2:
    for i in range(valor2,valor1):
        if i % 2 == 0:
            print(i)
else:
    for i in range(valor1,valor2):
        if i % 2 == 0:
            print(i)
