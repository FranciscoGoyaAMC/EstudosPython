"""
 Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
def maior_valor(*num):
    if len(num) == 0:
        print('Foram passados 0 valores')
    else:
        maior_numero = max(num)
        menor_numero = min(num)
        print(f'Maior valor: {maior_numero}')
        print(f'Menor valor: {menor_numero}')
