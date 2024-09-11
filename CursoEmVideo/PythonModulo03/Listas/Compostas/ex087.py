"""
Aprimore o exercício 86 mostrando no final:
A soma de todos valores digitados
A soma de todos os pares
A soma de todos os imprares
A soma de todos valores da terceira coluna
O maior valor da segunda linha
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_matriz = soma_pares = soma_impares = soma_terceira_coluna = maior_valor_segunda_linha = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor para [{l},{c}]: '))
print('MATRIZ: ')
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end='')
        soma_matriz += matriz[l][c]
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        else:
            soma_impares += matriz[l][c]
        if c == 2:
            soma_terceira_coluna += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maior_valor_segunda_linha:
                maior_valor_segunda_linha = matriz[l][c]
    print()
print(f'A soma de todos os valores da matriz é: {soma_matriz}')
print(f'A soma de todos os valores pares da matriz é: {soma_pares}')
print(f'A soma de todos os valores impares da matriz é: {soma_impares}')
print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior_valor_segunda_linha}')
