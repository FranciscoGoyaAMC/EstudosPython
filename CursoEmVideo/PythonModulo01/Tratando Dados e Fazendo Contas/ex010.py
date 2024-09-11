"""
Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considere o valor do dólar como 3.27
"""
from time import sleep

print('\033[1;34m-=\033[m' * 15)
print('\033[1;30mCONVERSOR DE REAIS PARA DÓLAR\033[m')
print('\033[1;34m-=\033[m' * 15)

cores = {'limpa':'\033[m',
         'verde':'\033[1;32m'}

n = float(input('Digite o valor em reais: '))

print('Calculando...')
sleep(2)

print(f'Com {cores["verde"]}{n:.2f}{cores["limpa"]} reais, você pode comprar {cores["verde"]}{n/3.27:.2f}{cores["limpa"]} dólares.')
