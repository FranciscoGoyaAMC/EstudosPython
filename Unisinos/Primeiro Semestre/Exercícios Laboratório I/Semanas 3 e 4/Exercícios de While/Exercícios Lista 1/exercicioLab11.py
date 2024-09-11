cont = 0
valor1 = int(input('Digite um número: '))
valor2 = int(input('Digite outro número: '))

somaPares = 0
somaImpares = 0

if valor1 < valor2:
    cont = valor1
    while cont < valor2:
        if cont % 2 == 0:
            somaPares += cont
        else:
            somaImpares += cont
        cont += 1
    print(f'A soma dos números pares entre {valor1} e {valor2} é {somaPares}')
    print(f'A soma dos números ímpares entre {valor1} e {valor2} é {somaImpares}')
else:
    print('Erro! Primeiro número deve ser inferior ao segundo.')
