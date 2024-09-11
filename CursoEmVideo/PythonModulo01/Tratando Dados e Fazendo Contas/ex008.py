"""
Faça um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""
from time import sleep

cores = {'limpa':'\033[m',
         'vermelho':'\033[31m'}

m = float(input('Digite um valor em metros: '))

print('Calculando...')
sleep(2)

print(f'{cores["vermelho"]}{m:.2f}{cores["limpa"]} metros em centímetros é {cores["vermelho"]}{m*100:.0f}{cores["limpa"]}. O valor em milímetros é {cores["vermelho"]}{m*1000:.0f}{cores["limpa"]}')
