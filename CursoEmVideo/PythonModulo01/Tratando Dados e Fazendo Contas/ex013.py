"""
Faça um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
from time import sleep

cores = {'limpa':'\033[m',
         'verde':'\033[1;32m'}

sal = float(input('Digite o salário: '))

print('Calculando...')
sleep(2)

print(f'O salário com aumento é {cores["verde"]}{sal + (sal * 0.15):.2f}{cores["limpa"]} reais.')
