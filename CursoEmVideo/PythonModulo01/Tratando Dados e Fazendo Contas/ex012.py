"""
Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""
from time import sleep

cores = {'limpa':'\033[m',
         'verde':'\033[1;32m'}

p = float(input('Digite o valor do produto: '))

print('Calculando...')
sleep(2)

print(f'O valor com desconto é {cores["verde"]}{p - (p * 0.05):.2f}{cores["limpa"]} reais.')
