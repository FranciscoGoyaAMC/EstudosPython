"""
 Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
def maior_valor(*num):
    if len(num) == 0:
        print('Foram passados 0 valores')
    else:
        maior_numero = num[0]
        menor_numero = num[0]
        print(f'Você digitou {len(num)} valores')
        for v in range(0, len(num)):
            if num[v] > maior_numero:
                maior_numero = num[v]
            if num[v] < menor_numero:
                menor_numero = num[v]
        print(f'O maior valor digitado foi {maior_numero}')
        print(f'O menor valor digitado foi {menor_numero}')
